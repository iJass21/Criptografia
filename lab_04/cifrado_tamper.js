// ==UserScript==
// @name         Cifrar mensajes
// @namespace    https://ejemplo.com
// @version      1.0
// @description  Descifrar mensajes cifrados en divs con 3DES ECB y mostrarlos en texto plano en consola
// @match        https://cripto.tiiny.site/*
// @grant        unsafeWindow
// @require https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js#sha512-E8QSvWZ0eCLGk4km3hxSsNmGWbLtSCSUcewDQPQWZF6pEU8GlT8a5fF32wOl1i8ftdMhssTrF/OhyGWwonTcXA==
// ==/UserScript==

(function() {


    // Texto a cifrar
    const textoACifrar = 'equipo';

    // Definir la clave en formato hexadecimal
    const keyHex = '53454755524f53454755524f53454755524f53454755524f';

    // Convertir la clave a un objeto WordArray
    const key = CryptoJS.enc.Hex.parse(keyHex);

    const iv = CryptoJS.enc.Hex.parse('0000000000000000');

    // Realizar el cifrado utilizando 3DES
    const mensajeCifrado = CryptoJS.TripleDES.encrypt(textoACifrar, key, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7,
        iv: iv // Asegúrate de definir el IV si es necesario
    });

    // Mostrar el resultado del cifrado
    console.log("Mensaje cifrado:", mensajeCifrado.toString());


})();