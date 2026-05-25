// // ==UserScript==
// // @name         Uber V133 - LITE VIDEO (FINAL BYPASS)
// // @run-at       document-start
// // @match        :///*
// // @grant        none
// // ==/UserScript==

// (function() {
//     'use strict';
//     if (window._V133_FINAL) return;
//     window._V133_FINAL = true;

//     const cv = document.createElement('canvas');
//     const cx = cv.getContext('2d', { alpha: false, desynchronized: true });
//     cv.width = 720; cv.height = 1280;
    
//     const v = document.createElement('video');
//     v.muted = true; v.loop = true; v.playsInline = true;
//     v.setAttribute('webkit-playsinline', 'true');

//     let media = null;
//     let isV = false;
//     let st = { z: 1.5, x: 0, y: -120, t: 0, live: true };

//     function montar() {
//         if (document.getElementById('lite-ui')) return;
//         const ui = document.createElement('div');
//         ui.id = 'lite-ui';
//         ui.style = "position:fixed!important;top:0!important;left:0!important;width:100%!important;z-index:2147483647!important;background:#000!important;border-bottom:1px solid #00E5FF!important;padding:5px!important;text-align:center!important;";
        
//         ui.innerHTML = `
//             <input type="file" id="f" accept="image/,video/" style="width:95%;color:#00E5FF;font-size:12px;margin-bottom:5px;">
//             <div style="display:flex;justify-content:center;gap:2px;flex-wrap:wrap;">
//                 <button class="bt" onclick="window._v(1)">Z+</button>
//                 <button class="bt" onclick="window._v(2)">Z-</button>
//                 <button class="bt" onclick="window._v(5)">◀️</button>
//                 <button class="bt" onclick="window._v(6)">▶️</button>
//                 <button class="bt" onclick="window._v(3)">▲</button>
//                 <button class="bt" onclick="window._v(4)">▼</button>
//                 <button id="pl" onclick="window._v(7)" style="padding:10px;background:#f80;color:#fff;display:none;border:none;border-radius:4px;font-weight:bold;">PLAY</button>
//                 <button id="lv" onclick="window._v(8)" style="padding:10px;background:#0c5;color:#fff;border:none;border-radius:4px;font-weight:bold;">LIVE</button>
//             </div>
//             <style>.bt{padding:12px!important;background:#111!important;color:#00E5FF!important;border:1px solid #00E5FF!important;min-width:50px!important;font-weight:bold!important;border-radius:4px!important;}</style>
//         `;
//         (document.body || document.documentElement).appendChild(ui);

//         document.getElementById('f').onchange = (e) => {
//             const file = e.target.files[0];
//             if(!file) return;
//             const url = URL.createObjectURL(file);
//             if (file.type.startsWith('video/')) {
//                 isV = true; v.src = url;
//                 v.onloadedmetadata = () => { 
//                     media = v; v.play(); 
//                     document.getElementById('pl').style.display = 'block';
//                 };
//             } else {
//                 isV = false; const i = new Image();
//                 i.onload = () => { media = i; document.getElementById('pl').style.display = 'none'; };
//                 i.src = url;
//             }
//         };
//     }

//     window._v = (n) => {
//         if(n==1) st.z+=0.1; if(n==2) st.z-=0.1;
//         if(n==3) st.y-=30; if(n==4) st.y+=30;
//         if(n==5) st.x-=30; if(n==6) st.x+=30;
//         if(n==7 && isV) v.play();
//         if(n==8) { st.live = !st.live; document.getElementById('lv').style.background = st.live ? "#0c5" : "#d22"; }
//     };

//     function loop() {
//         cx.fillStyle = "#000";
//         cx.fillRect(0, 0, cv.width, cv.height);
//         if (media) {
//             st.t += 0.04;
//             const mw = isV ? v.videoWidth : media.width;
//             const mh = isV ? v.videoHeight : media.height;
//             if (mw && mh) {
//                 let s = Math.max(cv.width / mw, cv.height / mh) * st.z;
//                 let shakeX = st.live ? (Math.sin(st.t * 0.8) * 2 + Math.cos(st.t * 1.2) * 1) : 0;
//                 let shakeY = st.live ? (Math.cos(st.t * 0.7) * 3 + Math.sin(st.t * 1.1) * 1) : 0;
                
//                 cx.save();
//                 cx.translate(cv.width, 0); cx.scale(-1, 1);
//                 cx.drawImage(media, (cv.width - mw*s)/2 + st.x + shakeX, (cv.height - mh*s)/2 + st.y + shakeY, mw*s, mh*s);
                
//                 // Adiciona um ruído digital quase invisível para quebrar detecção de imagem estática
//                 if (st.live) {
//                     cx.globalAlpha = 0.01;
//                     cx.fillStyle = Math.random() > 0.5 ? "#fff" : "#000";
//                     cx.fillRect(Math.random() * cv.width, Math.random() * cv.height, 2, 2);
//                     cx.globalAlpha = 1.0;
//                 }
                
//                 cx.restore();
//             }
//         }
//         requestAnimationFrame(loop);
//     }

//     const originalGetUserMedia = navigator.mediaDevices.getUserMedia.bind(navigator.mediaDevices);
//     const originalEnumerateDevices = navigator.mediaDevices.enumerateDevices.bind(navigator.mediaDevices);
//     const originalToString = Function.prototype.toString;

//     const camuflar = (fn, originalFn) => {
//         return new Proxy(fn, {
//             get: (target, prop) => {
//                 if (prop === 'toString') return () => originalToString.call(originalFn);
//                 return target[prop];
//             }
//         });
//     };

//     const hook = () => {
//         if (navigator.mediaDevices._h) return;
//         navigator.mediaDevices._h = true;

//         // Disfarce de Enumerate Devices para parecer hardware legítimo
//         navigator.mediaDevices.enumerateDevices = camuflar(async () => {
//             const devices = await originalEnumerateDevices();
//             return devices.map(d => {
//                 if (d.kind === 'videoinput') {
//                     // Mantém os labels originais mas garante que a nossa câmera fake herde um deles
//                     return d;
//                 }
//                 return d;
//             });
//         }, originalEnumerateDevices);

//         const patchedGUM = async function(c) {
//             if (!c || !c.video || !media) return originalGetUserMedia(c);
//             try {
//                 const realStream = await originalGetUserMedia(c);
//                 const fakeStream = cv.captureStream(30);
//                 const fakeTrack = fakeStream.getVideoTracks()[0];
//                 const realTrack = realStream.getVideoTracks()[0];

//                 // Herança profunda de propriedades do hardware
//                 const trackProps = ['label', 'id', 'enabled', 'readyState'];
//                 trackProps.forEach(prop => {
//                     try {
//                         Object.defineProperty(fakeTrack, prop, {
//                             get: () => realTrack[prop],
//                             configurable: true
//                         });
//                     } catch(e) {}
//                 });

//                 fakeTrack.getSettings = () => realTrack.getSettings();
//                 fakeTrack.getCapabilities = () => realTrack.getCapabilities();

//                 realStream.removeTrack(realTrack);
//                 realStream.addTrack(fakeTrack);
//                 return realStream;
//             } catch (e) {
//                 return originalGetUserMedia(c);
//             }
//         };

//         navigator.mediaDevices.getUserMedia = camuflar(patchedGUM, originalGetUserMedia);
//     };

//     loop();
//     setInterval(() => { montar(); hook(); }, 1500);
//     window.addEventListener('touchstart', montar, {once:true});
// })();

// // ==UserScript==
// // @name         Uber V133 - LITE VIDEO (FINAL BYPASS) [FIXED]
// // @run-at       document-start
// // @match        *://*/*
// // @grant        none
// // ==/UserScript==

// (function() {
//     'use strict';
//     if (window._V133_FINAL) return;
//     window._V133_FINAL = true;

//     const cv = document.createElement('canvas');
//     const cx = cv.getContext('2d', { alpha: false, desynchronized: true });
//     cv.width = 720; cv.height = 1280;

//     const v = document.createElement('video');
//     v.muted = true; v.loop = true; v.playsInline = true;
//     v.setAttribute('webkit-playsinline', 'true');

//     let media = null;
//     let isV = false;

//     let st = { z: 1.5, x: 0, y: 0, t: 0, live: true };

//     function montar() {
//         if (document.getElementById('lite-ui')) return;
//         const ui = document.createElement('div');
//         ui.id = 'lite-ui';
//         ui.style = "position:fixed!important;top:0!important;left:0!important;width:100%!important;z-index:2147483647!important;background:#000!important;border-bottom:1px solid #00E5FF!important;padding:5px!important;text-align:center!important;";

//         ui.innerHTML = `
//             <input type="file" id="f" accept="image/*,video/*" style="width:95%;color:#00E5FF;font-size:12px;margin-bottom:5px;">
//             <div style="display:flex;justify-content:center;gap:2px;flex-wrap:wrap;">
//                 <button class="bt" onclick="window._v(1)">Z+</button>
//                 <button class="bt" onclick="window._v(2)">Z-</button>
//                 <button class="bt" onclick="window._v(5)">◀️</button>
//                 <button class="bt" onclick="window._v(6)">▶️</button>
//                 <button class="bt" onclick="window._v(3)">▲</button>
//                 <button class="bt" onclick="window._v(4)">▼</button>
//                 <button id="pl" onclick="window._v(7)" style="padding:10px;background:#f80;color:#fff;display:none;border:none;border-radius:4px;font-weight:bold;">PLAY</button>
//                 <button id="lv" onclick="window._v(8)" style="padding:10px;background:#0c5;color:#fff;border:none;border-radius:4px;font-weight:bold;">LIVE</button>
//             </div>
//             <style>.bt{padding:12px!important;background:#111!important;color:#00E5FF!important;border:1px solid #00E5FF!important;min-width:50px!important;font-weight:bold!important;border-radius:4px!important;}</style>
//         `;
//         (document.body || document.documentElement).appendChild(ui);

//         document.getElementById('f').onchange = (e) => {
//             const file = e.target.files[0];
//             if (!file) return;
//             const url = URL.createObjectURL(file);

//             if (file.type.startsWith('video/')) {
//                 isV = true;
//                 v.src = url;
//                 v.onloadedmetadata = () => {
//                     media = v;
//                     v.play();
//                     document.getElementById('pl').style.display = 'block';
//                 };
//             } else {
//                 isV = false;
//                 const img = new Image();
//                 img.onload = () => {
//                     // e gera um ImageBitmap sem rotação EXIF
//                     corrigirImagem(img, (bitmap) => {
//                         media = bitmap;
//                         st.x = 0; st.y = 0; st.z = 1.5;
//                         document.getElementById('pl').style.display = 'none';
//                     });
//                 };
//                 img.src = url;
//             }
//         };
//     }

//     function corrigirImagem(imgElement, callback) {
//         const tmp = document.createElement('canvas');
//         tmp.width = imgElement.naturalWidth;
//         tmp.height = imgElement.naturalHeight;
//         const tc = tmp.getContext('2d');
//         tc.drawImage(imgElement, 0, 0);
//         createImageBitmap(tmp).then(bitmap => {
//             callback(bitmap);
//         }).catch(() => {
//             // fallback se createImageBitmap não estiver disponível
//             callback(imgElement);
//         });
//     }

//     window._v = (n) => {
//         if (n == 1) st.z += 0.1;
//         if (n == 2) st.z -= 0.1;
//         if (n == 3) st.y -= 30;
//         if (n == 4) st.y += 30;
//         if (n == 5) st.x -= 30;
//         if (n == 6) st.x += 30;
//         if (n == 7 && isV) v.play();
//         if (n == 8) {
//             st.live = !st.live;
//             document.getElementById('lv').style.background = st.live ? "#0c5" : "#d22";
//         }
//     };

//     function loop() {
//         cx.fillStyle = "#000";
//         cx.fillRect(0, 0, cv.width, cv.height);

//         if (media) {
//             st.t += 0.04;

//             const mw = isV ? v.videoWidth : (media.width || media.naturalWidth);
//             const mh = isV ? v.videoHeight : (media.height || media.naturalHeight);

//             if (mw && mh) {
//                 let s = Math.max(cv.width / mw, cv.height / mh) * st.z;
//                 let shakeX = st.live ? (Math.sin(st.t * 0.8) * 2 + Math.cos(st.t * 1.2) * 1) : 0;
//                 let shakeY = st.live ? (Math.cos(st.t * 0.7) * 3 + Math.sin(st.t * 1.1) * 1) : 0;

//                 cx.save();

//                 // Imagem da galeria NÃO é espelhada para não inverter a foto
//                 if (isV) {
//                     cx.translate(cv.width, 0);
//                     cx.scale(-1, 1);
//                 }

//                 cx.drawImage(
//                     media,
//                     (cv.width - mw * s) / 2 + st.x + shakeX,
//                     (cv.height - mh * s) / 2 + st.y + shakeY,
//                     mw * s,
//                     mh * s
//                 );

//                 // Ruído digital quase invisível para quebrar detecção de imagem estática
//                 if (st.live) {
//                     cx.globalAlpha = 0.01;
//                     cx.fillStyle = Math.random() > 0.5 ? "#fff" : "#000";
//                     cx.fillRect(Math.random() * cv.width, Math.random() * cv.height, 2, 2);
//                     cx.globalAlpha = 1.0;
//                 }

//                 cx.restore();
//             }
//         }

//         requestAnimationFrame(loop);
//     }

//     const originalGetUserMedia = navigator.mediaDevices.getUserMedia.bind(navigator.mediaDevices);
//     const originalEnumerateDevices = navigator.mediaDevices.enumerateDevices.bind(navigator.mediaDevices);
//     const originalToString = Function.prototype.toString;

//     const camuflar = (fn, originalFn) => {
//         return new Proxy(fn, {
//             get: (target, prop) => {
//                 if (prop === 'toString') return () => originalToString.call(originalFn);
//                 return target[prop];
//             }
//         });
//     };

//     const hook = () => {
//         if (navigator.mediaDevices._h) return;
//         navigator.mediaDevices._h = true;

//         navigator.mediaDevices.enumerateDevices = camuflar(async () => {
//             const devices = await originalEnumerateDevices();
//             return devices.map(d => d);
//         }, originalEnumerateDevices);

//         const patchedGUM = async function(c) {
//             if (!c || !c.video || !media) return originalGetUserMedia(c);
//             try {
//                 const realStream = await originalGetUserMedia(c);
//                 const fakeStream = cv.captureStream(30);
//                 const fakeTrack = fakeStream.getVideoTracks()[0];
//                 const realTrack = realStream.getVideoTracks()[0];

//                 const trackProps = ['label', 'id', 'enabled', 'readyState'];
//                 trackProps.forEach(prop => {
//                     try {
//                         Object.defineProperty(fakeTrack, prop, {
//                             get: () => realTrack[prop],
//                             configurable: true
//                         });
//                     } catch(e) {}
//                 });

//                 fakeTrack.getSettings = () => realTrack.getSettings();
//                 fakeTrack.getCapabilities = () => realTrack.getCapabilities();

//                 realStream.removeTrack(realTrack);
//                 realStream.addTrack(fakeTrack);
//                 return realStream;
//             } catch (e) {
//                 return originalGetUserMedia(c);
//             }
//         };

//         navigator.mediaDevices.getUserMedia = camuflar(patchedGUM, originalGetUserMedia);
//     };

//     loop();
//     setInterval(() => { montar(); hook(); }, 1500);
//     window.addEventListener('touchstart', montar, { once: true });
// })();



(function() {
    'use strict';
    if (window._V133_FINAL) return;
    window._V133_FINAL = true;

    // Elementos de processamento em background
    const cv = document.createElement('canvas');
    const cx = cv.getContext('2d', { alpha: false, desynchronized: true });
    cv.width = 720; 
    cv.height = 1280;
    
    const v = document.createElement('video');
    v.muted = true; 
    v.loop = true; 
    v.playsInline = true;
    v.setAttribute('webkit-playsinline', 'true');

    let media = null;
    let isV = false;
    let st = { z: 1.5, x: 0, y: -120, t: 0, live: true };

    function montar() {
        if (document.getElementById('lite-ui')) return;
        const ui = document.createElement('div');
        ui.id = 'lite-ui';
        ui.style = "position:fixed!important;top:0!important;left:0!important;width:100%!important;z-index:2147483647!important;background:#000!important;border-bottom:1px solid #00E5FF!important;padding:5px!important;text-align:center!important;";
        
        ui.innerHTML = `
            <input type="file" id="f" accept="image/*,video/*" style="width:95%;color:#00E5FF;font-size:12px;margin-bottom:5px;">
            <div style="display:flex;justify-content:center;gap:2px;flex-wrap:wrap;">
                <button class="bt" onclick="window._v(1)">Z+</button>
                <button class="bt" onclick="window._v(2)">Z-</button>
                <button class="bt" onclick="window._v(5)">◀️</button>
                <button class="bt" onclick="window._v(6)">▶️</button>
                <button class="bt" onclick="window._v(3)">▲</button>
                <button class="bt" onclick="window._v(4)">▼</button>
                <button id="pl" onclick="window._v(7)" style="padding:10px;background:#f80;color:#fff;display:none;border:none;border-radius:4px;font-weight:bold;">PLAY</button>
                <button id="lv" onclick="window._v(8)" style="padding:10px;background:#0c5;color:#fff;border:none;border-radius:4px;font-weight:bold;">LIVE</button>
            </div>
            <style>.bt{padding:12px!important;background:#111!important;color:#00E5FF!important;border:1px solid #00E5FF!important;min-width:50px!important;font-weight:bold!important;border-radius:4px!important;}</style>
        `;
        (document.body || document.documentElement).appendChild(ui);

        document.getElementById('f').onchange = (e) => {
            const file = e.target.files[0];
            if(!file) return;
            const url = URL.createObjectURL(file);
            if (file.type.startsWith('video/')) {
                isV = true; 
                v.src = url;
                v.onloadedmetadata = () => { 
                    media = v; 
                    v.play().catch(err => console.log("Aguardando interação para dar play:", err)); 
                    document.getElementById('pl').style.display = 'block';
                };
            } else {
                isV = false; 
                const i = new Image();
                i.onload = () => { 
                    media = i; 
                    document.getElementById('pl').style.display = 'none'; 
                };
                i.src = url;
            }
        };
    }

    window._v = (n) => {
        if(n==1) st.z+=0.1; if(n==2) st.z-=0.1;
        if(n==3) st.y-=30; if(n==4) st.y+=30;
        if(n==5) st.x-=30; if(n==6) st.x+=30;
        if(n==7 && isV) v.play();
        if(n==8) { st.live = !st.live; document.getElementById('lv').style.background = st.live ? "#0c5" : "#d22"; }
    };

    function loop() {
    // Evita crashes se o canvas ainda não foi redimensionado pelo GUM
    if (cv.width === 0 || cv.height === 0) {
        requestAnimationFrame(loop);
        return;
    }

    cx.fillStyle = "#000";
    cx.fillRect(0, 0, cv.width, cv.height);
    
    if (media) {
        st.t += 0.04;
        const mw = isV ? v.videoWidth : media.width;
        const mh = isV ? v.videoHeight : media.height;
        if (mw && mh) {
            // Calcula o preenchimento mantendo a proporção correta
            let s = Math.max(cv.width / mw, cv.height / mh) * st.z;
            let shakeX = st.live ? (Math.sin(st.t * 0.8) * 1.5) : 0;
            let shakeY = st.live ? (Math.cos(st.t * 0.7) * 1.5) : 0;
            
            cx.save();
            // Importante: Alinhamento centralizado dinâmico
            cx.translate(cv.width, 0); 
            cx.scale(-1, 1); 
            cx.drawImage(media, (cv.width - mw*s)/2 + st.x + shakeX, (cv.height - mh*s)/2 + st.y + shakeY, mw*s, mh*s);
            
            if (st.live) {
                cx.globalAlpha = 0.008; // Ruído sutil adaptado para resoluções dinâmicas
                cx.fillStyle = Math.random() > 0.5 ? "#fff" : "#000";
                cx.fillRect(Math.random() * cv.width, Math.random() * cv.height, 3, 3);
                cx.globalAlpha = 1.0;
            }
            cx.restore();
        }
    }
    requestAnimationFrame(loop);
}

// ... (dentro de hook -> patchedGUM)
const patchedGUM = async function(c) {
    if (!c || !c.video) return originalGetUserMedia(c);
    try {
        const realStream = await originalGetUserMedia(c);
        const realTrack = realStream.getVideoTracks()[0];
        
        // CORREÇÃO GEOMÉTRICA: Captura as configurações exatas do hardware real
        const settings = realTrack.getSettings();
        cv.width = settings.width || 640;
        cv.height = settings.height || 480;
        console.log(`[RedTeam] Canvas adaptado para a resolução alvo: ${cv.width}x${cv.height}`);

        const fakeStream = cv.captureStream(settings.frameRate || 30);
        const fakeTrack = fakeStream.getVideoTracks()[0];

        const trackProps = ['label', 'id', 'enabled', 'readyState'];
        trackProps.forEach(prop => {
            try {
                Object.defineProperty(fakeTrack, prop, {
                    get: () => realTrack[prop],
                    configurable: true
                });
            } catch(e) {}
        });

        fakeTrack.getSettings = () => realTrack.getSettings();
        fakeTrack.getCapabilities = () => realTrack.getCapabilities();

        realStream.removeTrack(realTrack);
        realStream.addTrack(fakeTrack);
        
        // IMPORTANTE para persistência da análise: não mate a track real imediatamente 
        // se o SDK fizer checagem ativa de status de hardware no meio da validação.
        setTimeout(() => { realTrack.stop(); }, 5000); 

        return realStream;
    } catch (e) {
        return originalGetUserMedia(c);
    }
};

        navigator.mediaDevices.getUserMedia = camuflar(patchedGUM, originalGetUserMedia);
    };

    // Inicialização direta e única
    loop();
    montar();
    hook();
})();