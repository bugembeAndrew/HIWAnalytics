from django.shortcuts import render
from gis.models import Art
from gis.district import districts

# Create your views here.
def gis(request):
	patients = {}
	for i, value in districts.items():
	    if(i==1):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            maracha = {value:0}
	        maracha = {value:count}
	        patients.update(maracha)
	    elif(i==2):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            arua = {value:0}
	        arua = {value:count}
	        patients.update(arua)
	    elif(i==3):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            moyo = {value:0}
	        moyo = {value:count}
	        patients.update(moyo)
	    elif(i==4):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            adjumani = {value:0}
	        adjumani = {value:count}
	        patients.update(adjumani)
	    elif(i==5):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            nebbi = {value:0}
	        nebbi = {value:count}
	        patients.update(nebbi)
	    elif(i==6):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            yumbe = {value:0}
	        yumbe = {value:count}
	        patients.update(yumbe)
	    elif(i==7):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            zombo = {value:0}
	        zombo = {value:count}
	        patients.update(zombo)
	    elif(i==8):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            koboko = {value:0}
	        koboko = {value:count}
	        patients.update(koboko)
	    elif(i==9):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            apac = {value:0}
	        apac = {value:count}
	        patients.update(apac)
	    elif(i==10):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            gulu = {value:0}
	        gulu = {value:count}
	        patients.update(gulu)
	    elif(i==11):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kole = {value:0}
	        kole = {value:count}
	        patients.update(kole)
	    elif(i==12):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            nwoya = {value:0}
	        nwoya = {value:count}
	        patients.update(nwoya)
	    elif(i==13):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            agago = {value:0}
	        agago = {value:count}
	        patients.update(agago)
	    elif(i==14):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kitgum = {value:0}
	        kitgum = {value:count}
	        patients.update(kitgum)
	    elif(i==15):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            lira = {value:0}
	        lira = {value:count}
	        patients.update(lira)
	    elif(i==16):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            pader = {value:0}
	        pader = {value:count}
	        patients.update(pader)
	    elif(i==17):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            amolatar = {value:0}
	        amolatar = {value:count}
	        patients.update(amolatar)
	    elif(i==18):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            dokolo = {value:0}
	        dokolo = {value:count}
	        patients.update(dokolo)
	    elif(i==19):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            amuru = {value:0}
	        amuru = {value:count}
	        patients.update(amuru)
	    elif(i==20):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            oyam = {value:0}
	        oyam = {value:count}
	        patients.update(oyam)
	    elif(i==21):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            lamwo = {value:0}
	        lamwo = {value:count}
	        patients.update(lamwo)
	    elif(i==22):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            otuke = {value:0}
	        otuke = {value:count}
	        patients.update(otuke)
	    elif(i==23):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            alebtong = {value:0}
	        alebtong = {value:count}
	        patients.update(alebtong)
	    elif(i==24):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            bundibugyo = {value:0}
	        bundibugyo = {value:count}
	        patients.update(bundibugyo)
	    elif(i==25):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            hoima = {value:0}
	        hoima = {value:count}
	        patients.update(hoima)
	    elif(i==26):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kabarole = {value:0}
	        kabarole = {value:count}
	        patients.update(kabarole)
	    elif(i==27):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kasese = {value:0}
	        kasese = {value:count}
	        patients.update(kasese)
	    elif(i==28):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kibaale = {value:0}
	        kibaale = {value:count}
	        patients.update(kibaale)
	    elif(i==29):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            masindi = {value:0}
	        masindi = {value:count}
	        patients.update(masindi)
	    elif(i==30):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kamwenge = {value:0}
	        kamwenge = {value:count}
	        patients.update(kamwenge)
	    elif(i==31):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kyenjojo = {value:0}
	        kyenjojo = {value:count}
	        patients.update(kyenjojo)
	    elif(i==32):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            buliisa = {value:0}
	        buliisa = {value:count}
	        patients.update(buliisa)
	    elif(i==33):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kyegegwa = {value:0}
	        kyegegwa = {value:count}
	        patients.update(kyegegwa)
	    elif(i==34):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kiryandongo = {value:0}
	        kiryandongo = {value:count}
	        patients.update(kiryandongo)
	    elif(i==35):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            ntoroko = {value:0}
	        ntoroko = {value:count}
	        patients.update(ntoroko)
	    elif(i==36):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            mbarara = {value:0}
	        mbarara = {value:count}
	        patients.update(mbarara)
	    elif(i==37):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            ntungamo = {value:0}
	        ntungamo = {value:count}
	        patients.update(ntungamo)
	    elif(i==38):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            bushenyi = {value:0}
	        bushenyi = {value:count}
	        patients.update(bushenyi)
	    elif(i==39):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kabale = {value:0}
	        kabale = {value:count}
	        patients.update(kabale)
	    elif(i==40):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kisoro = {value:0}
	        kisoro = {value:count}
	        patients.update(kisoro)
	    elif(i==41):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            rukungiri = {value:0}
	        rukungiri = {value:count}
	        patients.update(rukungiri)
	    elif(i==42):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kanungu = {value:0}
	        kanungu = {value:count}
	        patients.update(kanungu)
	    elif(i==43):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            ibanda = {value:0}
	        ibanda = {value:count}
	        patients.update(ibanda)
	    elif(i==44):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            isingiro = {value:0}
	        isingiro = {value:count}
	        patients.update(isingiro)
	    elif(i==45):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kiruhura = {value:0}
	        kiruhura = {value:count}
	        patients.update(kiruhura)
	    elif(i==46):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            mitooma = {value:0}
	        mitooma = {value:count}
	        patients.update(mitooma)
	    elif(i==47):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            buhweju = {value:0}
	        buhweju = {value:count}
	        patients.update(buhweju)
	    elif(i==48):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            sheema = {value:0}
	        sheema = {value:count}
	        patients.update(sheema)
	    elif(i==49):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            rubirizi = {value:0}
	        rubirizi = {value:count}
	        patients.update(rubirizi)
	    elif(i==50):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            sironko = {value:0}
	        sironko = {value:count}
	        patients.update(sironko)
	    elif(i==51):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kamuli = {value:0}
	        kamuli = {value:count}
	        patients.update(kamuli)
	    elif(i==52):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            iganga = {value:0}
	        iganga = {value:count}
	        patients.update(iganga)
	    elif(i==53):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            jinja = {value:0}
	        jinja = {value:count}
	        patients.update(jinja)
	    elif(i==54):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            pallisa = {value:0}
	        pallisa = {value:count}
	        patients.update(pallisa)
	    elif(i==55):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            tororo = {value:0}
	        tororo = {value:count}
	        patients.update(tororo)
	    elif(i==56):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            mayuge = {value:0}
	        mayuge = {value:count}
	        patients.update(mayuge)
	    elif(i==57):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            bugiri = {value:0}
	        bugiri = {value:count}
	        patients.update(bugiri)
	    elif(i==58):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            busia = {value:0}
	        busia = {value:count}
	        patients.update(busia)
	    elif(i==59):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            butaleja = {value:0}
	        butaleja = {value:count}
	        patients.update(butaleja)
	    elif(i==60):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            manafwa = {value:0}
	        manafwa = {value:count}
	        patients.update(manafwa)
	    elif(i==61):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kaliro = {value:0}
	        kaliro = {value:count}
	        patients.update(kaliro)
	    elif(i==62):
	        count = Art.objects.filter(district=i).count()
	        budaka = {value:count}
	        patients.update(budaka)
	    elif(i==63):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            namutumba = {value:0}
	        namutumba = {value:count}
	        patients.update(namutumba)
	    elif(i==64):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            bududa = {value:0}
	        bududa = {value:count}
	        patients.update(bududa)
	    elif(i==65):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kibuku = {value:0}
	        kibuku = {value:count}
	        patients.update(kibuku)
	    elif(i==66):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            bulambuli = {value:0}
	        bulambuli = {value:count}
	        patients.update(bulambuli)
	    elif(i==67):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            mbale = {value:0}
	        mbale = {value:count}
	        patients.update(mbale)
	    elif(i==68):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            maracha = {value:0}
	        buyende = {value:count}
	        patients.update(buyende)
	    elif(i==69):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            luuka = {value:0}
	        luuka = {value:count}
	        patients.update(luuka)
	    elif(i==70):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            namayingo = {value:0}
	        namayingo = {value:count}
	        patients.update(namayingo)
	    elif(i==71):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kween = {value:0}
	        kween = {value:count}
	        patients.update(kween)
	    elif(i==72):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            napak = {value:0}
	        napak = {value:count}
	        patients.update(napak)
	    elif(i==73):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            ngora = {value:0}
	        ngora = {value:count}
	        patients.update(ngora)
	    elif(i==74):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kapchorwa = {value:0}
	        kapchorwa = {value:count}
	        patients.update(kapchorwa)
	    elif(i==75):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kotido = {value:0}
	        kotido = {value:count}
	        patients.update(kotido)
	    elif(i==76):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kumi = {value:0}
	        kumi = {value:count}
	        patients.update(kumi)
	    elif(i==77):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            moroto = {value:0}
	        moroto = {value:count}
	        patients.update(moroto)
	    elif(i==78):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            soroti = {value:0}
	        soroti = {value:count}
	        patients.update(soroti)
	    elif(i==79):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            katakwi = {value:0}
	        katakwi = {value:count}
	        patients.update(katakwi)
	    elif(i==80):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kaberamaido = {value:0}
	        kaberamaido = {value:count}
	        patients.update(kaberamaido)
	    elif(i==81):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            nakapiripirit = {value:0}
	        nakapiripirit = {value:count}
	        patients.update(nakapiripirit)
	    elif(i==82):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            amuria = {value:0}
	        amuria = {value:count}
	        patients.update(amuria)
	    elif(i==83):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            bukwo = {value:0}
	        bukwo = {value:count}
	        patients.update(bukwo)
	    elif(i==84):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kaabong = {value:0}
	        kaabong = {value:count}
	        patients.update(kaabong)
	    elif(i==85):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            serere = {value:0}
	        serere = {value:count}
	        patients.update(serere)
	    elif(i==86):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            abim = {value:0}
	        abim = {value:count}
	        patients.update(abim)
	    elif(i==87):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            amudat = {value:0}
	        amudat = {value:count}
	        patients.update(amudat)
	    elif(i==88):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            bukedea = {value:0}
	        bukedea = {value:count}
	        patients.update(bukedea)
	    elif(i==89):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kampala = {value:0}
	        kampala = {value:count}
	        patients.update(kampala)
	    elif(i==90):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kiboga = {value:0}
	        kiboga = {value:count}
	        patients.update(kiboga)
	    elif(i==91):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kayunga = {value:0}
	        kayunga = {value:count}
	        patients.update(kayunga)
	    elif(i==92):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            buvuma = {value:0}
	        buvuma = {value:count}
	        patients.update(buvuma)
	    elif(i==93):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            mukono = {value:0}
	        mukono = {value:count}
	        patients.update(mukono)
	    elif(i==94):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            nakasongola = {value:0}
	        nakasongola = {value:count}
	        patients.update(nakasongola)
	    elif(i==95):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            luweero = {value:0}
	        luweero = {value:count}
	        patients.update(luweero)
	    elif(i==96):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            buikwe = {value:0}
	        buikwe = {value:count}
	        patients.update(buikwe)
	    elif(i==97):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kyankwanzi = {value:0}
	        kyankwanzi = {value:count}
	        patients.update(kyankwanzi)
	    elif(i==98):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            nakaseke = {value:0}
	        nakaseke = {value:count}
	        patients.update(nakaseke)
	    elif(i==99):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kalungu = {value:0}
	        kalungu = {value:count}
	        patients.update(kalungu)
	    elif(i==100):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            lwengo = {value:0}
	        lwengo = {value:count}
	        patients.update(lwengo)
	    elif(i==101):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kalangala = {value:0}
	        kalangala = {value:count}
	        patients.update(kalangala)
	    elif(i==102):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            lyantonde = {value:0}
	        lyantonde = {value:count}
	        patients.update(lyantonde)
	    elif(i==103):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            wakiso = {value:0}
	        wakiso = {value:count}
	        patients.update(wakiso)
	    elif(i==104):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            gomba = {value:0}
	        gomba = {value:count}
	        patients.update(gomba)
	    elif(i==105):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            bukomansimbi = {value:0}
	        bukomansimbi = {value:count}
	        patients.update(bukomansimbi)
	    elif(i==106):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            butambala = {value:0}
	        butambala = {value:count}
	        patients.update(butambala)
	    elif(i==107):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            masaka = {value:0}
	        masaka = {value:count}
	        patients.update(masaka)
	    elif(i==108):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            mpigi = {value:0}
	        mpigi = {value:count}
	        patients.update(mpigi)
	    elif(i==109):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            rakai = {value:0}
	        rakai = {value:count}
	        patients.update(rakai)
	    elif(i==110):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            ssembabule = {value:0}
	        ssembabule = {value:count}
	        patients.update(ssembabule)
	    elif(i==111):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            mityana = {value:0}
	        mityana = {value:count}
	        patients.update(mityana)
	    elif(i==112):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            mubende = {value:0}
	        mubende = {value:count}
	        patients.update(mubende)
	    else:
	        print('Unknown district.')
	#data = js.dumps(patients)
	#return HttpResponse(data)
	template = 'gis/map.html'
	context = {'art_dict':patients}
	return render(request, template, context)

def density(request):
	patients = {}
	for i, value in districts.items():
	    if(i==1):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            maracha = {value:0}
	        maracha = {value:count}
	        patients.update(maracha)
	    elif(i==2):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            arua = {value:0}
	        arua = {value:count}
	        patients.update(arua)
	    elif(i==3):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            moyo = {value:0}
	        moyo = {value:count}
	        patients.update(moyo)
	    elif(i==4):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            adjumani = {value:0}
	        adjumani = {value:count}
	        patients.update(adjumani)
	    elif(i==5):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            nebbi = {value:0}
	        nebbi = {value:count}
	        patients.update(nebbi)
	    elif(i==6):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            yumbe = {value:0}
	        yumbe = {value:count}
	        patients.update(yumbe)
	    elif(i==7):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            zombo = {value:0}
	        zombo = {value:count}
	        patients.update(zombo)
	    elif(i==8):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            koboko = {value:0}
	        koboko = {value:count}
	        patients.update(koboko)
	    elif(i==9):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            apac = {value:0}
	        apac = {value:count}
	        patients.update(apac)
	    elif(i==10):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            gulu = {value:0}
	        gulu = {value:count}
	        patients.update(gulu)
	    elif(i==11):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kole = {value:0}
	        kole = {value:count}
	        patients.update(kole)
	    elif(i==12):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            nwoya = {value:0}
	        nwoya = {value:count}
	        patients.update(nwoya)
	    elif(i==13):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            agago = {value:0}
	        agago = {value:count}
	        patients.update(agago)
	    elif(i==14):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kitgum = {value:0}
	        kitgum = {value:count}
	        patients.update(kitgum)
	    elif(i==15):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            lira = {value:0}
	        lira = {value:count}
	        patients.update(lira)
	    elif(i==16):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            pader = {value:0}
	        pader = {value:count}
	        patients.update(pader)
	    elif(i==17):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            amolatar = {value:0}
	        amolatar = {value:count}
	        patients.update(amolatar)
	    elif(i==18):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            dokolo = {value:0}
	        dokolo = {value:count}
	        patients.update(dokolo)
	    elif(i==19):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            amuru = {value:0}
	        amuru = {value:count}
	        patients.update(amuru)
	    elif(i==20):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            oyam = {value:0}
	        oyam = {value:count}
	        patients.update(oyam)
	    elif(i==21):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            lamwo = {value:0}
	        lamwo = {value:count}
	        patients.update(lamwo)
	    elif(i==22):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            otuke = {value:0}
	        otuke = {value:count}
	        patients.update(otuke)
	    elif(i==23):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            alebtong = {value:0}
	        alebtong = {value:count}
	        patients.update(alebtong)
	    elif(i==24):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            bundibugyo = {value:0}
	        bundibugyo = {value:count}
	        patients.update(bundibugyo)
	    elif(i==25):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            hoima = {value:0}
	        hoima = {value:count}
	        patients.update(hoima)
	    elif(i==26):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kabarole = {value:0}
	        kabarole = {value:count}
	        patients.update(kabarole)
	    elif(i==27):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kasese = {value:0}
	        kasese = {value:count}
	        patients.update(kasese)
	    elif(i==28):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kibaale = {value:0}
	        kibaale = {value:count}
	        patients.update(kibaale)
	    elif(i==29):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            masindi = {value:0}
	        masindi = {value:count}
	        patients.update(masindi)
	    elif(i==30):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kamwenge = {value:0}
	        kamwenge = {value:count}
	        patients.update(kamwenge)
	    elif(i==31):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kyenjojo = {value:0}
	        kyenjojo = {value:count}
	        patients.update(kyenjojo)
	    elif(i==32):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            buliisa = {value:0}
	        buliisa = {value:count}
	        patients.update(buliisa)
	    elif(i==33):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kyegegwa = {value:0}
	        kyegegwa = {value:count}
	        patients.update(kyegegwa)
	    elif(i==34):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kiryandongo = {value:0}
	        kiryandongo = {value:count}
	        patients.update(kiryandongo)
	    elif(i==35):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            ntoroko = {value:0}
	        ntoroko = {value:count}
	        patients.update(ntoroko)
	    elif(i==36):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            mbarara = {value:0}
	        mbarara = {value:count}
	        patients.update(mbarara)
	    elif(i==37):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            ntungamo = {value:0}
	        ntungamo = {value:count}
	        patients.update(ntungamo)
	    elif(i==38):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            bushenyi = {value:0}
	        bushenyi = {value:count}
	        patients.update(bushenyi)
	    elif(i==39):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kabale = {value:0}
	        kabale = {value:count}
	        patients.update(kabale)
	    elif(i==40):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kisoro = {value:0}
	        kisoro = {value:count}
	        patients.update(kisoro)
	    elif(i==41):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            rukungiri = {value:0}
	        rukungiri = {value:count}
	        patients.update(rukungiri)
	    elif(i==42):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kanungu = {value:0}
	        kanungu = {value:count}
	        patients.update(kanungu)
	    elif(i==43):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            ibanda = {value:0}
	        ibanda = {value:count}
	        patients.update(ibanda)
	    elif(i==44):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            isingiro = {value:0}
	        isingiro = {value:count}
	        patients.update(isingiro)
	    elif(i==45):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kiruhura = {value:0}
	        kiruhura = {value:count}
	        patients.update(kiruhura)
	    elif(i==46):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            mitooma = {value:0}
	        mitooma = {value:count}
	        patients.update(mitooma)
	    elif(i==47):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            buhweju = {value:0}
	        buhweju = {value:count}
	        patients.update(buhweju)
	    elif(i==48):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            sheema = {value:0}
	        sheema = {value:count}
	        patients.update(sheema)
	    elif(i==49):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            rubirizi = {value:0}
	        rubirizi = {value:count}
	        patients.update(rubirizi)
	    elif(i==50):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            sironko = {value:0}
	        sironko = {value:count}
	        patients.update(sironko)
	    elif(i==51):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kamuli = {value:0}
	        kamuli = {value:count}
	        patients.update(kamuli)
	    elif(i==52):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            iganga = {value:0}
	        iganga = {value:count}
	        patients.update(iganga)
	    elif(i==53):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            jinja = {value:0}
	        jinja = {value:count}
	        patients.update(jinja)
	    elif(i==54):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            pallisa = {value:0}
	        pallisa = {value:count}
	        patients.update(pallisa)
	    elif(i==55):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            tororo = {value:0}
	        tororo = {value:count}
	        patients.update(tororo)
	    elif(i==56):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            mayuge = {value:0}
	        mayuge = {value:count}
	        patients.update(mayuge)
	    elif(i==57):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            bugiri = {value:0}
	        bugiri = {value:count}
	        patients.update(bugiri)
	    elif(i==58):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            busia = {value:0}
	        busia = {value:count}
	        patients.update(busia)
	    elif(i==59):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            butaleja = {value:0}
	        butaleja = {value:count}
	        patients.update(butaleja)
	    elif(i==60):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            manafwa = {value:0}
	        manafwa = {value:count}
	        patients.update(manafwa)
	    elif(i==61):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kaliro = {value:0}
	        kaliro = {value:count}
	        patients.update(kaliro)
	    elif(i==62):
	        count = Art.objects.filter(district=i).count()
	        budaka = {value:count}
	        patients.update(budaka)
	    elif(i==63):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            namutumba = {value:0}
	        namutumba = {value:count}
	        patients.update(namutumba)
	    elif(i==64):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            bududa = {value:0}
	        bududa = {value:count}
	        patients.update(bududa)
	    elif(i==65):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kibuku = {value:0}
	        kibuku = {value:count}
	        patients.update(kibuku)
	    elif(i==66):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            bulambuli = {value:0}
	        bulambuli = {value:count}
	        patients.update(bulambuli)
	    elif(i==67):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            mbale = {value:0}
	        mbale = {value:count}
	        patients.update(mbale)
	    elif(i==68):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            maracha = {value:0}
	        buyende = {value:count}
	        patients.update(buyende)
	    elif(i==69):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            luuka = {value:0}
	        luuka = {value:count}
	        patients.update(luuka)
	    elif(i==70):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            namayingo = {value:0}
	        namayingo = {value:count}
	        patients.update(namayingo)
	    elif(i==71):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kween = {value:0}
	        kween = {value:count}
	        patients.update(kween)
	    elif(i==72):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            napak = {value:0}
	        napak = {value:count}
	        patients.update(napak)
	    elif(i==73):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            ngora = {value:0}
	        ngora = {value:count}
	        patients.update(ngora)
	    elif(i==74):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kapchorwa = {value:0}
	        kapchorwa = {value:count}
	        patients.update(kapchorwa)
	    elif(i==75):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kotido = {value:0}
	        kotido = {value:count}
	        patients.update(kotido)
	    elif(i==76):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kumi = {value:0}
	        kumi = {value:count}
	        patients.update(kumi)
	    elif(i==77):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            moroto = {value:0}
	        moroto = {value:count}
	        patients.update(moroto)
	    elif(i==78):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            soroti = {value:0}
	        soroti = {value:count}
	        patients.update(soroti)
	    elif(i==79):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            katakwi = {value:0}
	        katakwi = {value:count}
	        patients.update(katakwi)
	    elif(i==80):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kaberamaido = {value:0}
	        kaberamaido = {value:count}
	        patients.update(kaberamaido)
	    elif(i==81):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            nakapiripirit = {value:0}
	        nakapiripirit = {value:count}
	        patients.update(nakapiripirit)
	    elif(i==82):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            amuria = {value:0}
	        amuria = {value:count}
	        patients.update(amuria)
	    elif(i==83):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            bukwo = {value:0}
	        bukwo = {value:count}
	        patients.update(bukwo)
	    elif(i==84):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kaabong = {value:0}
	        kaabong = {value:count}
	        patients.update(kaabong)
	    elif(i==85):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            serere = {value:0}
	        serere = {value:count}
	        patients.update(serere)
	    elif(i==86):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            abim = {value:0}
	        abim = {value:count}
	        patients.update(abim)
	    elif(i==87):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            amudat = {value:0}
	        amudat = {value:count}
	        patients.update(amudat)
	    elif(i==88):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            bukedea = {value:0}
	        bukedea = {value:count}
	        patients.update(bukedea)
	    elif(i==89):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kampala = {value:0}
	        kampala = {value:count}
	        patients.update(kampala)
	    elif(i==90):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kiboga = {value:0}
	        kiboga = {value:count}
	        patients.update(kiboga)
	    elif(i==91):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kayunga = {value:0}
	        kayunga = {value:count}
	        patients.update(kayunga)
	    elif(i==92):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            buvuma = {value:0}
	        buvuma = {value:count}
	        patients.update(buvuma)
	    elif(i==93):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            mukono = {value:0}
	        mukono = {value:count}
	        patients.update(mukono)
	    elif(i==94):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            nakasongola = {value:0}
	        nakasongola = {value:count}
	        patients.update(nakasongola)
	    elif(i==95):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            luweero = {value:0}
	        luweero = {value:count}
	        patients.update(luweero)
	    elif(i==96):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            buikwe = {value:0}
	        buikwe = {value:count}
	        patients.update(buikwe)
	    elif(i==97):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kyankwanzi = {value:0}
	        kyankwanzi = {value:count}
	        patients.update(kyankwanzi)
	    elif(i==98):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            nakaseke = {value:0}
	        nakaseke = {value:count}
	        patients.update(nakaseke)
	    elif(i==99):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kalungu = {value:0}
	        kalungu = {value:count}
	        patients.update(kalungu)
	    elif(i==100):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            lwengo = {value:0}
	        lwengo = {value:count}
	        patients.update(lwengo)
	    elif(i==101):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            kalangala = {value:0}
	        kalangala = {value:count}
	        patients.update(kalangala)
	    elif(i==102):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            lyantonde = {value:0}
	        lyantonde = {value:count}
	        patients.update(lyantonde)
	    elif(i==103):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            wakiso = {value:0}
	        wakiso = {value:count}
	        patients.update(wakiso)
	    elif(i==104):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            gomba = {value:0}
	        gomba = {value:count}
	        patients.update(gomba)
	    elif(i==105):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            bukomansimbi = {value:0}
	        bukomansimbi = {value:count}
	        patients.update(bukomansimbi)
	    elif(i==106):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            butambala = {value:0}
	        butambala = {value:count}
	        patients.update(butambala)
	    elif(i==107):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            masaka = {value:0}
	        masaka = {value:count}
	        patients.update(masaka)
	    elif(i==108):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            mpigi = {value:0}
	        mpigi = {value:count}
	        patients.update(mpigi)
	    elif(i==109):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            rakai = {value:0}
	        rakai = {value:count}
	        patients.update(rakai)
	    elif(i==110):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            ssembabule = {value:0}
	        ssembabule = {value:count}
	        patients.update(ssembabule)
	    elif(i==111):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            mityana = {value:0}
	        mityana = {value:count}
	        patients.update(mityana)
	    elif(i==112):
	        count = Art.objects.filter(district=i).count()
	        if(count==0):
	            mubende = {value:0}
	        mubende = {value:count}
	        patients.update(mubende)
	    else:
	        print('Unknown district.')
	#data = js.dumps(patients)
	#return HttpResponse(data)
	template = 'gis/density.html'
	context = {'art_dict':patients}
	return render(request, template, context)

