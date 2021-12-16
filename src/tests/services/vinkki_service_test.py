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

class TestVinkkiService(unittest.TestCase):
    def setUp(self):
        pass

    def test_tietokanta_on_aluksi_tyhja(self):
        fake_repo = FakeVinkkiRepository()
        service = VinkkiService(fake_repo)
        testlist = service.search_vinkkis()
        self.assertTrue(len(testlist)==0)

    def test_tietokanta_ei_ole_lisaamisen_jalkeen_tyhja_1(self):
        fake_repo = FakeVinkkiRepository()
        service = VinkkiService(fake_repo)
        service.create_vinkki("vinkki1", "url1", "testitekija")
        testlist = service.search_vinkkis()
        self.assertTrue(len(testlist)>0)

    def test_tietokanta_ei_ole_lisaamisen_jalkeen_tyhja_2(self):
        fake_repo = FakeVinkkiRepository()
        service = VinkkiService(fake_repo)
        service.create_vinkki("vinkki1", "url1", "testitekija")
        service.create_vinkki("vinkki2", "url2", "testitekija")
        service.create_vinkki("vinkki3", "url3", "toinentekija")
        testlist = service.search_vinkkis()
        self.assertTrue(len(testlist)>0)
    
    def test_haetaan_vain_omat_vinkit_1(self):
        fake_repo = FakeVinkkiRepository()
        service = VinkkiService(fake_repo)
        service.create_vinkki("vinkki1", "url1", "testitekija")
        service.create_vinkki("vinkki2", "url2", "testitekija")
        service.create_vinkki("vinkki3", "url3", "toinentekija")
        testlist = service.search_own_vinkkis("testitekija")
        self.assertTrue(len(testlist)>0)
    
    def test_haetaan_vain_omat_vinkit_2(self):
        fake_repo = FakeVinkkiRepository()
        service = VinkkiService(fake_repo)
        service.create_vinkki("vinkki1", "url1", "testitekija")
        service.create_vinkki("vinkki2", "url2", "testitekija")
        service.create_vinkki("vinkki3", "url3", "toinentekija")
        testlist = service.search_own_vinkkis("jokutekija")
        self.assertTrue(len(testlist)==0)
    
    def test_poistaminen_toimii_oikein_1(self):
        fake_repo = FakeVinkkiRepository()
        service = VinkkiService(fake_repo)
        service.create_vinkki("vinkki1", "url1", "testitekija")
        service.hide_vinkki("0")
        testlist = service.search_vinkkis()
        self.assertTrue(len(testlist)==0)
    
    def test_poistaminen_toimii_oikein_2(self):
        fake_repo = FakeVinkkiRepository()
        service = VinkkiService(fake_repo)
        service.create_vinkki("vinkki1", "url1", "testitekija")
        service.create_vinkki("vinkki2", "url2", "testitekija")
        service.create_vinkki("vinkki3", "url3", "toinentekija")
        service.hide_vinkki("0")
        service.hide_vinkki("1")
        service.hide_vinkki("2")
        testlist = service.search_vinkkis()
        self.assertTrue(len(testlist)==0)
    
    def test_poistaminen_toimii_oikein_2(self):
        fake_repo = FakeVinkkiRepository()
        service = VinkkiService(fake_repo)
        service.create_vinkki("vinkki1", "url1", "testitekija")
        service.create_vinkki("vinkki2", "url2", "testitekija")
        service.create_vinkki("vinkki3", "url3", "toinentekija")
        service.hide_vinkki("0")
        service.hide_vinkki("1")
        testlist = service.search_vinkkis()
        self.assertTrue(len(testlist)>0)
    
    def test_poistaminen_toimii_oikein_3(self):
        fake_repo = FakeVinkkiRepository()
        service = VinkkiService(fake_repo)
        service.create_vinkki("vinkki1", "url1", "testitekija")
        service.create_vinkki("vinkki2", "url2", "testitekija")
        service.create_vinkki("vinkki3", "url3", "toinentekija")
        service.hide_vinkki("0")
        testlist = service.search_own_vinkkis("testitekija")
        self.assertTrue(len(testlist)>0)
    
    def test_poistaminen_toimii_oikein_4(self):
        fake_repo = FakeVinkkiRepository()
        service = VinkkiService(fake_repo)
        service.create_vinkki("vinkki1", "url1", "testitekija")
        service.create_vinkki("vinkki2", "url2", "testitekija")
        service.create_vinkki("vinkki3", "url3", "toinentekija")
        service.hide_vinkki("0")
        service.hide_vinkki("1")
        testlist = service.search_own_vinkkis("testitekija")
        self.assertTrue(len(testlist)==0)

    def test_poistaminen_toimii_oikein_5(self):
        fake_repo = FakeVinkkiRepository()
        service = VinkkiService(fake_repo)
        service.create_vinkki("vinkki1", "url1", "testitekija")
        service.create_vinkki("vinkki2", "url2", "testitekija")
        service.create_vinkki("vinkki3", "url3", "toinentekija")
        service.hide_vinkki("0")
        service.hide_vinkki("1")
        testlist = service.search_own_vinkkis("toinentekija")
        self.assertTrue(len(testlist)>0)
    
    def test_poistaminen_toimii_oikein_5(self):
        fake_repo = FakeVinkkiRepository()
        service = VinkkiService(fake_repo)
        service.create_vinkki("vinkki1", "url1", "testitekija")
        service.create_vinkki("vinkki2", "url2", "testitekija")
        service.create_vinkki("vinkki3", "url3", "toinentekija")
        service.hide_vinkki("0")
        service.hide_vinkki("1")
        testlist = service.search_own_vinkkis("jokutekija")
        self.assertTrue(len(testlist)==0)
    
    def test_poistaminen_toimii_oikein_6(self):
        fake_repo = FakeVinkkiRepository()
        service = VinkkiService(fake_repo)
        service.create_vinkki("vinkki1", "url1", "testitekija")
        service.create_vinkki("vinkki2", "url2", "testitekija")
        service.create_vinkki("vinkki3", "url3", "toinentekija")
        service.hide_vinkki("3")
        service.hide_vinkki("4")
        testlist = service.search_vinkkis()
        self.assertTrue(len(testlist)>0)
    
    def test_paivays_toimii_1(self):
        fake_repo = FakeVinkkiRepository()
        service = VinkkiService(fake_repo)
        service.create_vinkki("vinkki1", "url1", "testitekija")
        service.set_read_vinkki("0")
        vinkki = fake_repo.vinkkis["0"]
        self.assertTrue(len(vinkki["paivays"])>0)
    
    def test_paivays_toimii_2(self):
        fake_repo = FakeVinkkiRepository()
        service = VinkkiService(fake_repo)
        service.create_vinkki("vinkki1", "url1", "testitekija")
        service.create_vinkki("vinkki2", "url2", "testitekija")
        service.create_vinkki("vinkki3", "url3", "toinentekija")
        service.set_read_vinkki("0")
        vinkki = fake_repo.vinkkis["1"]
        self.assertTrue(vinkki["paivays"]==None)
    
    def test_luetuksi_merkitseminen_toimii_1(self):
        fake_repo = FakeVinkkiRepository()
        service = VinkkiService(fake_repo)
        service.create_vinkki("vinkki1", "url1", "testitekija")
        service.set_read_vinkki("0")
        vinkki = fake_repo.vinkkis["0"]
        self.assertTrue(vinkki["luettu"]==True)
    
    def test_luetuksi_merkitseminen_toimii_2(self):
        fake_repo = FakeVinkkiRepository()
        service = VinkkiService(fake_repo)
        service.create_vinkki("vinkki1", "url1", "testitekija")
        service.create_vinkki("vinkki2", "url2", "testitekija")
        service.create_vinkki("vinkki3", "url3", "toinentekija")
        service.set_read_vinkki("0")
        vinkki = fake_repo.vinkkis["1"]
        self.assertTrue(vinkki["luettu"]==False)
    
    def test_lukemattomaksi_merkitseminen_toimii_1(self):
        fake_repo = FakeVinkkiRepository()
        service = VinkkiService(fake_repo)
        service.create_vinkki("vinkki1", "url1", "testitekija")
        service.set_read_vinkki("0")
        service.set_unread_vinkki("0")
        vinkki = fake_repo.vinkkis["0"]
        self.assertTrue(vinkki["luettu"]==False)
    
    def test_lukemattomaksi_merkitseminen_toimii_2(self):
        fake_repo = FakeVinkkiRepository()
        service = VinkkiService(fake_repo)
        service.create_vinkki("vinkki1", "url1", "testitekija")
        service.create_vinkki("vinkki2", "url2", "testitekija")
        service.create_vinkki("vinkki3", "url3", "toinentekija")
        service.set_read_vinkki("0")
        service.set_read_vinkki("1")
        service.set_unread_vinkki("0")
        vinkki = fake_repo.vinkkis["1"]
        self.assertTrue(vinkki["luettu"]==True)