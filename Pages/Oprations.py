import time

from selenium.webdriver.common.by import By
from Config.config import Testdata
from Pages.BasePage import BasePage
from Pages.checkstatus import CheckPageaction

class Oprations(BasePage):
    STATUSBUTTON = (By.XPATH, '//a[@href="/status"]')
    AUTOREFRACE =(By.XPATH,"//mat-grid-list/div/mat-grid-tile/figure/button[2]")
    CLIPVALUEONE=(By.XPATH,"//mat-tab-body[1]/div/div/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[1]/td[2]")
    CLIPVALUETWO=(By.XPATH,"//mat-tab-body[1]/div/div/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[2]/td[2]")
    CLIPVALUETHREE=(By.XPATH,"//mat-tab-body[1]/div/div/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[3]/td[2]")
    CLIPVALUEFORE=(By.XPATH,"//mat-tab-body[1]/div/div/mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[4]/td[2]")
    OPRATIONONE=(By.XPATH,"//mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[1]/td[7]/span")
    OPRATIONTWO=(By.XPATH,"//mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[2]/td[7]/span")
    OPRATIONTHREE=(By.XPATH,"//mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[3]/td[7]/span")
    OPRATIONFORE=(By.XPATH,"//mat-sidenav-container/mat-sidenav-content/div/table/tbody/tr[4]/td[7]/span")
    STATUSONEONE=(By.XPATH,"//mat-sidenav-content/div/table/tbody/tr[1]/td[10]/span")
    STATUSONETWO=(By.XPATH,"//mat-sidenav-content/div/table/tbody/tr[2]/td[10]/span")
    STATUSONETHREE=(By.XPATH,"//mat-sidenav-content/div/table/tbody/tr[3]/td[10]/span")
    STATUSONEFORE=(By.XPATH,"//mat-sidenav-content/div/table/tbody/tr[4]/td[10]/span")
    
    def Qc_Check(self):
        print(CheckPageaction.filecopyforopration())
        time.sleep(5)
        time.sleep(4)
        self.do_click(self.STATUSBUTTON)
        self.do_click(self.AUTOREFRACE)
        time.sleep(4)
        while True:                
            self.do_click(self.AUTOREFRACE)
            time.sleep(2)
            out =self.get_element_text(self.CLIPVALUEONE)
            out = out.split('\n')
            if(out[3]=="automationtesting" and self.get_element_text(self.OPRATIONONE)=='QC' and self.get_element_text(self.STATUSONEONE)=="Running"):
                time.sleep(5)    
            else:
                outone=self.get_element_text(self.CLIPVALUETWO)
                outone = outone.split('\n')
                if(outone[3]=="automationtesting" and self.get_element_text(self.OPRATIONTWO)=='QC' and self.get_element_text(self.STATUSONETWO)=="Ok"):
                    return "Ok"
                outone=self.get_element_text(self.CLIPVALUETHREE)
                outone = outone.split('\n')
                if(outone[3]=="automationtesting" and self.get_element_text(self.OPRATIONTHREE)=='QC' and self.get_element_text(self.STATUSONETHREE)=="Ok"):
                    return "Ok"
                outone=self.get_element_text(self.CLIPVALUEFORE)
                outone = outone.split('\n')
                if(outone[3]=="automationtesting" and self.get_element_text(self.OPRATIONFORE)=='QC' and self.get_element_text(self.STATUSONEFORE)=="Ok"):
                    return "Ok"
                outone=self.get_element_text(self.CLIPVALUEONE)
                outone = outone.split('\n')
                if(outone[3]=="automationtesting" and self.get_element_text(self.OPRATIONONE)=='QC' and self.get_element_text(self.OPRATIONONE)=="Ok"):
                    return "Ok"
    
    def Move_Check(self):
        # print(CheckPageaction.filecopyforopration())
        time.sleep(5)
        time.sleep(4)
        self.do_click(self.STATUSBUTTON)
        self.do_click(self.AUTOREFRACE)
        time.sleep(4)
        while True:                
            self.do_click(self.AUTOREFRACE)
            time.sleep(2)
            out =self.get_element_text(self.CLIPVALUEONE)
            out = out.split('\n')
            if(out[3]=="automationtesting" and self.get_element_text(self.OPRATIONONE)=='Move' and self.get_element_text(self.STATUSONEONE)=="Running"):
                time.sleep(5)    
            else:
                outone=self.get_element_text(self.CLIPVALUETWO)
                outone = outone.split('\n')
                if(outone[3]=="automationtesting" and self.get_element_text(self.OPRATIONTWO)=='Move' and self.get_element_text(self.STATUSONETWO)=="Ok"):
                    return "Ok"
                outone=self.get_element_text(self.CLIPVALUETHREE)
                outone = outone.split('\n')
                if(outone[3]=="automationtesting" and self.get_element_text(self.OPRATIONTHREE)=='Move' and self.get_element_text(self.STATUSONETHREE)=="Ok"):
                    return "Ok"
                outone=self.get_element_text(self.CLIPVALUEFORE)
                outone = outone.split('\n')
                if(outone[3]=="automationtesting" and self.get_element_text(self.OPRATIONFORE)=='Move' and self.get_element_text(self.STATUSONEFORE)=="Ok"):
                    return "Ok"
                outone=self.get_element_text(self.CLIPVALUEONE)
                outone = outone.split('\n')
                if(outone[3]=="automationtesting" and self.get_element_text(self.OPRATIONONE)=='Move' and self.get_element_text(self.OPRATIONONE)=="Ok"):
                    return "Ok"
    def Move_Check_pending(self):
        # print(CheckPageaction.filecopyforopration())
        time.sleep(5)
        time.sleep(4)
        self.do_click(self.STATUSBUTTON)
        self.do_click(self.AUTOREFRACE)
        time.sleep(4)
        while True:                
            self.do_click(self.AUTOREFRACE)
            time.sleep(2)
            out =self.get_element_text(self.CLIPVALUEONE)
            out = out.split('\n')
            if(out[3]=="automationtesting" and self.get_element_text(self.OPRATIONONE)=='Move' and self.get_element_text(self.STATUSONEONE)=="Running"):
                time.sleep(5)    
            else:
                outone=self.get_element_text(self.CLIPVALUETWO)
                outone = outone.split('\n')
                if(outone[3]=="automationtesting" and self.get_element_text(self.OPRATIONTWO)=='Move' and self.get_element_text(self.STATUSONETWO)=="Ok"):
                    return "Ok"
                outone=self.get_element_text(self.CLIPVALUETHREE)
                outone = outone.split('\n')
                if(outone[3]=="automationtesting" and self.get_element_text(self.OPRATIONTHREE)=='Move' and self.get_element_text(self.STATUSONETHREE)=="Ok"):
                    return "Ok"
                outone=self.get_element_text(self.CLIPVALUEFORE)
                outone = outone.split('\n')
                if(outone[3]=="automationtesting" and self.get_element_text(self.OPRATIONFORE)=='Move' and self.get_element_text(self.STATUSONEFORE)=="Ok"):
                    return "Ok"
                outone=self.get_element_text(self.CLIPVALUEONE)
                outone = outone.split('\n')
                if(outone[3]=="automationtesting" and self.get_element_text(self.OPRATIONONE)=='Move' and self.get_element_text(self.OPRATIONONE)=="Ok"):
                    return "Ok"
                
    def Proxy_Check(self):
        # print(CheckPageaction.filecopyforopration())
        time.sleep(5)
        time.sleep(4)
        self.do_click(self.STATUSBUTTON)
        self.do_click(self.AUTOREFRACE)
        time.sleep(4)
        while True:                
            self.do_click(self.AUTOREFRACE)
            time.sleep(2)
            out =self.get_element_text(self.CLIPVALUEONE)
            out = out.split('\n')
            if(out[3]=="automationtesting" and self.get_element_text(self.OPRATIONONE)=='Proxy' and self.get_element_text(self.STATUSONEONE)=="Running"):
                time.sleep(5)    
            else:
                outone=self.get_element_text(self.CLIPVALUETWO)
                outone = outone.split('\n')
                if(outone[3]=="automationtesting" and self.get_element_text(self.OPRATIONTWO)=='Proxy' and self.get_element_text(self.STATUSONETWO)=="Ok"):
                    return "Ok"
                outone=self.get_element_text(self.CLIPVALUETHREE)
                outone = outone.split('\n')
                if(outone[3]=="automationtesting" and self.get_element_text(self.OPRATIONTHREE)=='Proxy' and self.get_element_text(self.STATUSONETHREE)=="Ok"):
                    return "Ok"
                outone=self.get_element_text(self.CLIPVALUEFORE)
                outone = outone.split('\n')
                if(outone[3]=="automationtesting" and self.get_element_text(self.OPRATIONFORE)=='Proxy' and self.get_element_text(self.STATUSONEFORE)=="Ok"):
                    return "Ok"
                outone=self.get_element_text(self.CLIPVALUEONE)
                outone = outone.split('\n')
                if(outone[3]=="automationtesting" and self.get_element_text(self.OPRATIONONE)=='Proxy' and self.get_element_text(self.OPRATIONONE)=="Ok"):
                    return "Ok"
    
    
    def media_qc(self):
        pass
