# Plan SEO i Google Maps – Pokoje Gościnne w Kamyku (V54)

## Fakty obiektu
Prawdziwy adres: ul. Stefana Żeromskiego 87, 42-125 Kamyk. W ofercie wg materiałów: 7 pokoi, 19 miejsc; ok. 6 km do Kłobucka, ok. 15 km do Częstochowy. Sprawdzić z właścicielką przed wdrożeniem telefon, udogodnienia i odległości. Nie twierdzić, że obiekt leży w Częstochowie albo Kłobucku.

## Mapowanie fraz (jeden główny temat na stronę)

| Strona | Zamiar wyszukiwania | Przykładowe frazy |
|---|---|---|
| / | Rozpoznanie obiektu, nocleg w rejonie obu miast | pokoje gościnne Kłobuck Częstochowa, noclegi okolice Kłobucka |
| noclegi-klobuck.html | Nocleg w pobliżu Kłobucka | noclegi Kłobuck, pokoje Kłobuck, noclegi okolice Kłobucka |
| noclegi-czestochowa.html | Nocleg poza Częstochową | noclegi Częstochowa, noclegi pod Częstochową, pokoje okolice Częstochowy |
| noclegi-pracownicze-kamyk.html | Noclegi dla ekip i firm | kwatery pracownicze Kłobuck, noclegi pracownicze Częstochowa, pokoje dla firm |
| noclegi-dla-pielgrzymow.html | Pobyty związane z Jasną Górą | noclegi dla pielgrzymów Częstochowa, nocleg pod Częstochową Jasna Góra |

Nie tworzyć kolejnych podstron tylko dla wariantów tego samego zapytania. Uzupełniać realne informacje i zdjęcia, zamiast upychać słowa kluczowe.

## Google Business Profile – połączenie z SEO organicznym
1. Nazwa firmy powinna dokładnie odpowiadać rzeczywistej nazwie używanej na szyldzie i w działalności. Nie dopisywać fraz „noclegi Częstochowa Kłobuck” do nazwy tylko dla SEO.
2. Adres podawać wyłącznie rzeczywisty. Zweryfikować właściwą kategorię obiektu i warunki kwalifikacji do profilu; noclegi powinny mieć odpowiednią kategorię zakwaterowania.
3. Uzupełnić telefon, stronę, godziny kontaktu (jeżeli prawdziwe), udogodnienia, zasady przyjazdu, autentyczne fotografie pokoi i wejścia.
4. Pozyskiwać wyłącznie prawdziwe opinie od gości, bez nagradzania za recenzje; odpowiadać na pytania i opinie.
5. Dodać adres strony z parametrami UTM (opcjonalnie): https://DOMENA.PL/?utm_source=google&utm_medium=organic&utm_campaign=profil_firmy (nie używać jako kanonicznego URL).
6. Mapy Google zależą m.in. od trafności, odległości i rozpoznawalności. Lokalizacja w Kamyku może ograniczyć widoczność na zapytania z centrum Częstochowy.

## Po wybraniu domeny
1. W folderze strony wykonać `python publish_seo.py https://DOMENA.PL` (Python 3, bez bibliotek zewnętrznych).
2. Wgrać całą zawartość folderu, również `.htaccess` na Apache/LiteSpeed. Na Nginx/innym hostingu osobno skonfigurować przekierowanie /noclegi-kobuck.html -> /noclegi-klobuck.html (301) i wersję www/non-www.
3. Sprawdzić 200 dla 5 podstron, 301 dla starego błędnego URL, 404 dla nieistniejących, HTTPS i unikalne canonical.
4. W Google Search Console zweryfikować domenę, przesłać `/sitemap.xml`, sprawdzić indeksację. Bez publikacji nie można uzyskać organicznych pozycji.
5. Sprawdzić Google Rich Results Test oraz validator.schema.org; dane `LodgingBusiness` nie gwarantują rozszerzonego wyniku.
6. Zmierzyć PageSpeed Insights / Lighthouse na urządzeniach mobilnych po publikacji; skontrolować LCP, CLS, INP, jakość zdjęć i formularz WhatsApp.
7. Dodać wiarygodne wzmianki o obiekcie w miejscowych katalogach/portalach i na mapach – bez farm linków.
8. Co 30 dni analizować Search Console: zapytania, strony, CTR, wyświetlenia, pozycję, telefony i zapytania o rezerwacje.

## Wymaga potwierdzenia z klientką
Prawdziwa nazwa obiektu, prawo do używania fotografii, nr telefonu, 7 pokoi/19 miejsc, łazienki, klimatyzacja, kuchnia, pralka, parking dla busów, pobyty na jedną noc, warunki płatności, faktury, regulamin, zgody prywatności / cookies jeśli dojdzie analityka. Obecny formularz tylko konstruuje wiadomość WhatsApp, nie wysyła danych na serwer.

## Pomiary
`MONITORING_FRAZ.csv` jest arkuszem startowym – to plan śledzenia, nie fałszywe dane o pozycjach. Monitorować też konwersję: kliknięcia numeru telefonu i przejścia do WhatsApp po poprawnym wdrożeniu analityki oraz zgód, jeśli wymagane.
