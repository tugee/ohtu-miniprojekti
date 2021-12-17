import unittest
from datetime import datetime
from services.vinkki_service import VinkkiService

class FakeVinkkiRepository:
    def __init__(self):
        self.vinkkis = {}
        self.counter = 0

    def find_by_vinkki(self):
        resultlist = []
        for vinkki in self.vinkkis:
            vinkkicontents = self.vinkkis[vinkki]
            if vinkkicontents["piilotettu"]==False:
                resultlist.append(vinkki)
        return resultlist
    
    def find_by_user(self, tekija):
        resultlist = []
        for vinkki in self.vinkkis:
            vinkkicontents = self.vinkkis[vinkki]
            if vinkkicontents["piilotettu"]==False and vinkkicontents["tekija"]==tekija:
                resultlist.append(vinkki)
        return resultlist

    def create(self, nimi, url, tekija):
        id = str(self.counter)
        self.vinkkis[id] = {"nimi": nimi, "url": url, "tekija": tekija, "luettu": False, "paivays": None, "piilotettu": False}
        self.counter+=1

    def hide(self, id):
        if id not in self.vinkkis.keys():
            return
        vinkki = self.vinkkis[id]
        vinkki["piilotettu"] = True

    def set_read(self, id):
        if id not in self.vinkkis.keys():
            return
        vinkki = self.vinkkis[id]
        vinkki["luettu"] = True

    def set_read_date(self, id):
        if id not in self.vinkkis.keys():
            return
        date = datetime.now()
        finaldate = date.strftime("%x")
        vinkki = self.vinkkis[id]
        vinkki["paivays"] = finaldate

    def set_unread(self, id):
        if id not in self.vinkkis.keys():
            return
        vinkki = self.vinkkis[id]
        vinkki["luettu"] = False

class TestVinkkiServiceEmpty(unittest.TestCase):
    def test_tietokanta_on_aluksi_tyhja(self):
        fake_repo = FakeVinkkiRepository()
        service = VinkkiService(fake_repo)
        testlist = service.search_vinkkis()
        self.assertTrue(len(testlist)==0)
class TestVinkkiService(unittest.TestCase):
    def setUp(self):
        self.fake_repo = FakeVinkkiRepository()
        self.service = VinkkiService(self.fake_repo)
        self.service.create_vinkki("vinkki1", "url1", "testitekija")

    def test_tietokanta_ei_ole_lisaamisen_jalkeen_tyhja_1(self):
        testlist = self.service.search_vinkkis()
        self.assertTrue(len(testlist)>0)

    def test_tietokantaan_voi_lisata_useamman_vinkin(self):
        self.service.create_vinkki("vinkki2", "url2", "testitekija")
        testlist = self.service.search_vinkkis()
        self.assertTrue(len(testlist)>0)
    
    def test_haetaan_vain_omat_vinkit_1(self):
        self.service.create_vinkki("vinkki3", "url3", "toinentekija")
        testlist = self.service.search_own_vinkkis("testitekija")
        self.assertTrue(len(testlist)==1)
    
    def test_haetaan_vain_omat_vinkit_paulauttaa_tyhjan_jos_ei_loydy(self):
        testlist = self.service.search_own_vinkkis("jokutekija")
        self.assertTrue(len(testlist)==0)
    
    def test_poistaminen_toimii_oikein_1(self):
        self.service.hide_vinkki("0")
        testlist = self.service.search_vinkkis()
        self.assertTrue(len(testlist)==0)
    
    def test_poistaminen_toimii_oikein_2(self):
        self.service.create_vinkki("vinkki2", "url2", "testitekija")
        self.service.create_vinkki("vinkki3", "url3", "toinentekija")
        self.service.hide_vinkki("0")
        self.service.hide_vinkki("1")
        self.service.hide_vinkki("2")
        testlist = self.service.search_vinkkis()
        self.assertTrue(len(testlist)==0)
    
    def test_poistaminen_toimii_oikein_2(self):
        self.service.create_vinkki("vinkki2", "url2", "testitekija")
        self.service.create_vinkki("vinkki3", "url3", "toinentekija")
        self.service.hide_vinkki("0")
        self.service.hide_vinkki("1")
        testlist = self.service.search_vinkkis()
        self.assertTrue(len(testlist)==1)
    
    def test_poistaminen_toimii_oikein_3(self):
        self.service.create_vinkki("vinkki2", "url2", "testitekija")
        self.service.create_vinkki("vinkki3", "url3", "toinentekija")
        self.service.hide_vinkki("0")
        testlist = self.service.search_own_vinkkis("testitekija")
        self.assertTrue(len(testlist)==1)
    
    def test_poistaminen_toimii_oikein_4(self):
        self.service.create_vinkki("vinkki2", "url2", "testitekija")
        self.service.create_vinkki("vinkki3", "url3", "toinentekija")
        self.service.hide_vinkki("0")
        self.service.hide_vinkki("1")
        testlist = self.service.search_own_vinkkis("testitekija")
        self.assertTrue(len(testlist)==0)

    def test_omien_vinkkien_poistaminen_ei_poista_toisten_vinkkeja(self):
        self.service.create_vinkki("vinkki2", "url2", "testitekija")
        self.service.create_vinkki("vinkki3", "url3", "toinentekija")
        self.service.hide_vinkki("0")
        self.service.hide_vinkki("1")
        testlist = self.service.search_own_vinkkis("toinentekija")
        self.assertTrue(len(testlist)==1)
    
    def test_poistaminen_ei_lisaa_uudelle_kayttajalle_vinkkeja(self):
        self.service.create_vinkki("vinkki2", "url2", "testitekija")
        self.service.create_vinkki("vinkki3", "url3", "toinentekija")
        self.service.hide_vinkki("0")
        self.service.hide_vinkki("1")
        testlist = self.service.search_own_vinkkis("jokutekija")
        self.assertTrue(len(testlist)==0)
    
    def test_poistaminen_toimii_oikein_6(self):
        self.service.create_vinkki("vinkki2", "url2", "testitekija")
        self.service.create_vinkki("vinkki3", "url3", "toinentekija")
        self.service.hide_vinkki("3")
        self.service.hide_vinkki("4")
        testlist = self.service.search_vinkkis()
        self.assertTrue(len(testlist)>0)
    
    def test_paivays_toimii_1(self):
        self.service.set_read_vinkki("0")
        vinkki = self.fake_repo.vinkkis["0"]
        self.assertTrue(len(vinkki["paivays"])>0)
    
    def test_paivays_toimii_2(self):
        self.service.create_vinkki("vinkki2", "url2", "testitekija")
        self.service.create_vinkki("vinkki3", "url3", "toinentekija")
        self.service.set_read_vinkki("0")
        vinkki = self.fake_repo.vinkkis["1"]
        self.assertTrue(vinkki["paivays"]==None)
    
    def test_luetuksi_merkitseminen_toimii_1(self):
        self.service.set_read_vinkki("0")
        vinkki = self.fake_repo.vinkkis["0"]
        self.assertTrue(vinkki["luettu"]==True)
    
    def test_luetuksi_merkitseminen_toimii_2(self):
        self.service.create_vinkki("vinkki2", "url2", "testitekija")
        self.service.create_vinkki("vinkki3", "url3", "toinentekija")
        self.service.set_read_vinkki("0")
        vinkki = self.fake_repo.vinkkis["1"]
        self.assertTrue(vinkki["luettu"]==False)
    
    def test_lukemattomaksi_merkitseminen_toimii_1(self):
        self.service.set_read_vinkki("0")
        self.service.set_unread_vinkki("0")
        vinkki = self.fake_repo.vinkkis["0"]
        self.assertTrue(vinkki["luettu"]==False)
    
    def test_lukemattomaksi_merkitseminen_toimii_2(self):
        self.service.create_vinkki("vinkki2", "url2", "testitekija")
        self.service.create_vinkki("vinkki3", "url3", "toinentekija")
        self.service.set_read_vinkki("0")
        self.service.set_read_vinkki("1")
        self.service.set_unread_vinkki("0")
        vinkki = self.fake_repo.vinkkis["1"]
        self.assertTrue(vinkki["luettu"]==True)