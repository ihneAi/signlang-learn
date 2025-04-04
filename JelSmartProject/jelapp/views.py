from django.shortcuts import render, get_object_or_404
from .models import Kezikonyv, Gyakorlo, Fogalom
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

def home(request):
    return render(request, 'index.html')

def kezikonyvek(request):
    kezikonyvek_lista = [
        {
            'cim': 'Jelnyelv Tanítás',
            'leiras': 'Alkalmazási útmutató a jelnyelvhez',
            'kategoria': 'Alapok'
        },
        {
            'cim': 'Nejcse jelnyelv - Kulturális tárgyalás',
            'leiras': 'Nejcse jelnyelvi kifejezések nyelvi, kulturális és történelmi háttere',
            'kategoria': 'Kulturális'
        },
        # További demo tartalmak...
    ]
    return render(request, 'kezikonyvek.html', {'kezikonyvek': kezikonyvek_lista})


def gyakorlok(request):
    try:
        # Próbáljuk lekérni az adatbázisból
        gyakorlok_lista = list(Gyakorlo.objects.all())
        if not gyakorlok_lista:
            # Ha nincs adat, demo tartalmat jelenítünk meg
            gyakorlok_lista = [
                {
                    'cim': 'Jelnyelvi szókincs gyarapítása',
                    'leiras': 'Napi gyakorlatok a szókincs bővítéséhez',
                    'nehezseg': 'Kezdő'
                },
                {
                    'cim': 'Alapvető mondatszerkezetek',
                    'leiras': 'Gyakorló feladatok az alapvető mondatszerkezetek elsajátításához',
                    'nehezseg': 'Kezdő'
                },
                {
                    'cim': 'Beszélgetés gyakorlás',
                    'leiras': 'Párbeszédek gyakorlása különböző helyzetekben',
                    'nehezseg': 'Középhaladó'
                }
            ]
    except Exception as e:
        # Ha hiba történne (pl. tábla még nem létezik)
        gyakorlok_lista = [
            {
                'cim': 'Jelnyelvi szókincs gyarapítása',
                'leiras': 'Napi gyakorlatok a szókincs bővítéséhez',
                'nehezseg': 'Kezdő'
            },
            {
                'cim': 'Alapvető mondatszerkezetek',
                'leiras': 'Gyakorló feladatok az alapvető mondatszerkezetek elsajátításához',
                'nehezseg': 'Kezdő'
            }
        ]

    return render(request, 'gyakorlok.html', {'gyakorlok': gyakorlok_lista})


def fogalmak(request):
    try:
        # Alap lekérdezés
        fogalmak_lista = Fogalom.objects.all().order_by('nev')

        # Keresés kezelése
        keresesi_szo = request.GET.get('q', '').strip()
        if keresesi_szo:
            fogalmak_lista = fogalmak_lista.filter(
                Q(nev__icontains=keresesi_szo) |
                Q(definicio__icontains=keresesi_szo)
            )

        # Kategória szűrés
        kategoria = request.GET.get('kategoria')
        if kategoria and kategoria != 'összes':
            fogalmak_lista = fogalmak_lista.filter(kategoria=kategoria)

        # Kategóriák listája (csak a szűrt fogalmak kategóriáit mutatjuk)
        kategoriak = fogalmak_lista.values_list('kategoria', flat=True).distinct()

        # Oldalozás
        page = request.GET.get('page', 1)
        paginator = Paginator(fogalmak_lista, 10)  # 10 elem oldalanként

        try:
            fogalmak_paged = paginator.page(page)
        except PageNotAnInteger:
            fogalmak_paged = paginator.page(1)
        except EmptyPage:
            fogalmak_paged = paginator.page(paginator.num_pages)

        context = {
            'fogalmak': fogalmak_paged,
            'kategoriak': kategoriak,
            'keresesi_szo': keresesi_szo,
            'kivalasztott_kategoria': kategoria,
        }

        return render(request, 'fogalmak.html', context)

    except Exception as e:
        # Hibakezelés: naplózhatnánk a hibát és felhasználóbarát üzenetet jeleníthetnénk meg
        return render(request, 'fogalmak.html', {
            'error': 'Hiba történt a fogalmak betöltése közben',
            'kategoriak': [],
            'fogalmak': []
        })

def fogalom_reszletek(request, fogalom_id):
    fogalom = get_object_or_404(Fogalom, id=fogalom_id)
    return render(request, 'fogalom_reszletek.html', {'fogalom': fogalom})

def resztudas(request):
    return render(request, 'resztudas.html')