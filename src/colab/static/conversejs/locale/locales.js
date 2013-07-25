/*
 * This file specifies the language dependencies.
 *
 * Translations take up a lot of space and you are therefore advised to remove
 * from here any languages that you don't need.
 */

(function (root, factory) {
    require.config({
        paths: {
            "jed": "Libraries/jed",
            "af": "locale/af/LC_MESSAGES/af",
            "en": "locale/en/LC_MESSAGES/en",
            "es": "locale/es/LC_MESSAGES/es",
            "de": "locale/de/LC_MESSAGES/de",
            "hu": "locale/hu/LC_MESSAGES/hu",
            "it": "locale/it/LC_MESSAGES/it",
            "ptbr": "locale/pt_BR/LC_MESSAGES/pt-br"
        }
    });

    define("locales", [
        'jed',
        'af',
        'en',
        'es',
        'de',
        'hu',
        "it",
        'ptbr'
        ], function (jed, af, en, es, de, hu, it, ptbr) {
            root.locales = {};
            root.locales.af = af;
            root.locales.en = en;
            root.locales.es = es;
            root.locales.de = de;
            root.locales.hu = hu;
            root.locales.it = it;
            root.locales.ptbr = ptbr;
        });
})(this);
