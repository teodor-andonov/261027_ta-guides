/* TA PWA update worker v1. Append to sw.js (classic or module). */
(() => {
  let updating = false;
  self.addEventListener('message', event => {
    if (event.data?.type !== 'TA_UPDATE_APPLY') return;
    const reply = accepted => event.ports[0]?.postMessage({accepted});
    if (updating || !event.source?.url?.startsWith(self.registration.scope)) { reply(false); return; }
    updating = true;
    event.waitUntil((async () => {
      let windows = [];
      try {
        windows = (await self.clients.matchAll({type:'window',includeUncontrolled:true}))
          .filter(client => client.url.startsWith(self.registration.scope));
        if (!windows.length) { reply(false); return; }
        const ready = await Promise.all(windows.map(client => new Promise(resolve => {
          const channel = new MessageChannel();
          const timeout = setTimeout(() => { channel.port1.close(); resolve(false); },2000);
          channel.port1.onmessage = message => {
            clearTimeout(timeout); channel.port1.close(); resolve(message.data?.ready === true);
          };
          client.postMessage({type:'TA_UPDATE_PREPARE'},[channel.port2]);
        })));
        if (!ready.every(Boolean)) {
          windows.forEach(client => client.postMessage({type:'TA_UPDATE_CANCEL'}));
          reply(false); return;
        }
        reply(true);
        await self.skipWaiting();
      } catch {
        windows.forEach(client => client.postMessage({type:'TA_UPDATE_CANCEL'}));
        reply(false);
      } finally { updating = false; }
    })());
  });
})();
