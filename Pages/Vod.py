import time

from selenium.webdriver.common.by import By
from Config.config import Testdata
from Pages.BasePage import BasePage

class Vod(BasePage):
    PROFILEBUTTON = (By.XPATH, '//a[@href="/profile"]')
    VODBUTTON = (By.XPATH, '//mat-tab-group/mat-tab-header/div[2]/div/div/div[5]')
    ADDNEW = (By.XPATH, "//app-vodprofile/div/div/div[2]/button")
    TC=(By.XPATH,"//mat-expansion-panel[1]/div/div/mat-form-field[1]/div/div[1]/div/mat-select")
    TCVALUE = (By.XPATH, "//*[@Value='YES']")
    PROFILENAME = (By.XPATH, "//*[@Placeholder='Profile Name']")
    LOGOOVERLAY = (By.XPATH, "//*[@Placeholder='Logo Overlay Path']")
    IDENTPATH = (By.XPATH, "//*[@Placeholder='Ident Path']")
    OUTPUTEX = (By.XPATH, "//mat-form-field[6]/div/div[1]/div/mat-select")
    OUTPUTVALUE = (By.XPATH, "//*[@Value='.mxf']")
    PROFILE = (By.XPATH, "//mat-form-field[7]/div/div[1]/div/mat-select")
    PROFILEVALUE = (By.XPATH, "//*[@Value='high']")
    LEVEL=(By.XPATH,"//mat-expansion-panel[1]/div/div/mat-form-field[8]/div/div[1]/div/mat-select")
    LEVELVALUE = (By.XPATH, "//*[@Value='41']")
    SCALE_G=(By.XPATH,"//mat-form-field[9]/div/div[1]/div/mat-select")
    SCALE_GVALUE = (By.XPATH, "//*[@Value='100']")
    MUXRATE=(By.XPATH,"//mat-form-field[10]/div/div[1]/div/mat-select")
    MUXRATEVALUE = (By.XPATH, "//*[@Value='8.5M']")
    SUBTITLE=(By.XPATH,"//mat-form-field[11]/div/div[1]/div/mat-select")
    SUBTITLEVALUE = (By.XPATH, "//*[@Value='YES']")
    SUBTITLEPATH = (By.XPATH, "//*[@Placeholder='Subtitle Path']")
    SUBTITLEPATHLANGUAGE = (By.XPATH, "//*[@Placeholder='Subtitle Language']")
    REMARK = (By.XPATH, "//*[@Placeholder='Remarks']")
    AUDIOPARAMETERS = (By.XPATH,"//mat-expansion-panel[2]/mat-expansion-panel-header")
    PICELFORMET =(By.XPATH,"//mat-expansion-panel[2]/div/div/mat-form-field[1]/div/div[1]/div/mat-select")
    PICELFORMETVALUE = (By.XPATH, "//*[@Value='yuv420p']")
    SIMPLERATE= (By.XPATH,"//mat-expansion-panel[2]/div/div/mat-form-field[2]/div/div[1]/div/mat-select")
    SIMPLERATEVALUE = (By.XPATH, "//*[@Value='48000']")
    AUDIOCODEC=(By.XPATH,"//mat-accordion/mat-expansion-panel[2]/div/div/mat-form-field[3]/div/div[1]/div/mat-select")
    AUDIOCODECVALUE = (By.XPATH, "//*[@Value='DemuxAudio']")
    AUDIOBITRATE = (By.XPATH, "//*[@Placeholder='Audio Bitrate']")
    VIDEOPARAMETERS =(By.XPATH,"//mat-expansion-panel[3]/mat-expansion-panel-header")
    FRAMERATE=(By.XPATH,"//mat-expansion-panel[3]/div/div/mat-form-field[1]/div/div[1]/div/mat-select")
    FRAMERATEVALUE = (By.XPATH, "//*[@Value='25']")
    VIDEOCODEC=(By.XPATH,"//mat-expansion-panel[3]/div/div/mat-form-field[2]/div/div[1]/div/mat-select")
    VIDEOCODECVALUE=(By.XPATH, "//*[@Value='DemuxVideo']")
    RESOLUTION=(By.XPATH,"//mat-expansion-panel[3]/div/div/mat-form-field[3]/div/div[1]/div/mat-select")
    RESOLUTIONVALUE=(By.XPATH, "//*[@Value='1920x1080']")
    CONCATVIDEOCODEC = (By.XPATH, "//*[@Placeholder='Concat Video Codec']")
    VIDEOBITRATE = (By.XPATH, "//*[@Placeholder='Video Bitrate']")
    MINBITRATE = (By.XPATH, "//*[@Placeholder='Min Bitrate']")
    MAXBITRATE = (By.XPATH, "//*[@Placeholder='Max Bitrate']")
    OTHER =(By.XPATH,"//mat-expansion-panel[4]/mat-expansion-panel-header")
    EXTRAPARAMETER = (By.XPATH, "//*[@Placeholder='Extra Parameter']")
    ALERT_MESSAGE = (By.XPATH, "/html/body/div[3]/div/div/snack-bar-container/simple-snack-bar/span")
    SAVEBUTTON=(By.XPATH,"//app-vodprofile/div/div/div[3]/div/button[1]")
    UPDATEDATA=(By.XPATH,"//app-vodprofile/div/div/div[2]/table/tbody/tr/td[normalize-space(text())='automationtesting']")
    UPDATEDATA_NEW=(By.XPATH,"//app-vodprofile/div/div/div[2]/table/tbody/tr/td[normalize-space(text())='automationtesting']")
    UPDATEDATA_BUTTON=(By.XPATH,"//transfer/div/div/div[3]/div/button[1]")
    DELETEBUTTON = (By.XPATH,"//app-vodprofile/div/div/div[2]/table/tbody/tr/td[normalize-space(text())='automationtesting']/following-sibling::td/button")
    YESBUTTON=(By.XPATH,"//mat-dialog-container/dialog-vodprofile/div[2]/button[2]")
    
    def Add_vod_withouttc(self):
        time.sleep(2)
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        time.sleep(6)
        self.do_click(self.ADDNEW)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
    
    def Add_vod_withtc(self):
        time.sleep(2)
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        time.sleep(4)
        self.do_click(self.ADDNEW)
        self.do_click(self.TC)
        time.sleep(2)
        self.do_click(self.TCVALUE)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
            
    def Add_vod_withprofile(self,profilename,logovderlay,identpath):
        time.sleep(2)
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        time.sleep(4)
        self.do_click(self.ADDNEW)
        self.do_click(self.TC)
        time.sleep(2)
        self.do_click(self.TCVALUE)
        self.do_send_keys(self.PROFILENAME,profilename)
        self.do_send_keys(self.LOGOOVERLAY,logovderlay)
        self.do_send_keys(self.IDENTPATH,identpath)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
            
    def Add_vod_withoutputextention(self,profilename,logovderlay,identpath):
        time.sleep(2)
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        time.sleep(4)
        self.do_click(self.ADDNEW)
        self.do_click(self.TC)
        time.sleep(2)
        self.do_click(self.TCVALUE)
        self.do_send_keys(self.PROFILENAME,profilename)
        self.do_send_keys(self.LOGOOVERLAY,logovderlay)
        self.do_send_keys(self.IDENTPATH,identpath)
        self.do_click(self.OUTPUTEX)
        self.do_click(self.OUTPUTVALUE)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)   
           
    def Add_vod_withvprofile(self,profilename,logovderlay,identpath):
        time.sleep(2)
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        time.sleep(4)
        self.do_click(self.ADDNEW)
        self.do_click(self.TC)
        time.sleep(2)
        self.do_click(self.TCVALUE)
        self.do_send_keys(self.PROFILENAME,profilename)
        self.do_send_keys(self.LOGOOVERLAY,logovderlay)
        self.do_send_keys(self.IDENTPATH,identpath)
        self.do_click(self.OUTPUTEX)
        self.do_click(self.OUTPUTVALUE)
        self.do_click(self.PROFILE)
        self.do_click(self.PROFILEVALUE)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
        
    def Add_vod_withlevel(self,profilename,logovderlay,identpath):
        time.sleep(2)
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        time.sleep(4)
        self.do_click(self.ADDNEW)
        self.do_click(self.TC)
        time.sleep(2)
        self.do_click(self.TCVALUE)
        self.do_send_keys(self.PROFILENAME,profilename)
        self.do_send_keys(self.LOGOOVERLAY,logovderlay)
        self.do_send_keys(self.IDENTPATH,identpath)
        self.do_click(self.OUTPUTEX)
        time.sleep(1)
        self.do_click(self.OUTPUTVALUE)
        self.do_click(self.PROFILE)
        time.sleep(1)
        self.do_click(self.PROFILEVALUE)
        self.do_click(self.LEVEL)
        time.sleep(1)
        self.do_click(self.LEVELVALUE)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
         
    def Add_vod_withscale(self,profilename,logovderlay,identpath):
        time.sleep(2)
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        time.sleep(4)
        self.do_click(self.ADDNEW)
        self.do_click(self.TC)
        time.sleep(2)
        self.do_click(self.TCVALUE)
        self.do_send_keys(self.PROFILENAME,profilename)
        self.do_send_keys(self.LOGOOVERLAY,logovderlay)
        self.do_send_keys(self.IDENTPATH,identpath)
        self.do_click(self.OUTPUTEX)
        time.sleep(1)
        self.do_click(self.OUTPUTVALUE)
        self.do_click(self.PROFILE)
        time.sleep(1)
        self.do_click(self.PROFILEVALUE)
        self.do_click(self.LEVEL)
        time.sleep(1)
        self.do_click(self.LEVELVALUE)
        self.do_click(self.SCALE_G)
        time.sleep(1)
        self.do_click(self.SCALE_GVALUE)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
        
            
    def Add_vod_withmuxrate(self,profilename,logovderlay,identpath):
        time.sleep(2)
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        time.sleep(4)
        self.do_click(self.ADDNEW)
        self.do_click(self.TC)
        time.sleep(2)
        self.do_click(self.TCVALUE)
        self.do_send_keys(self.PROFILENAME,profilename)
        self.do_send_keys(self.LOGOOVERLAY,logovderlay)
        self.do_send_keys(self.IDENTPATH,identpath)
        self.do_click(self.OUTPUTEX)
        time.sleep(1)
        self.do_click(self.OUTPUTVALUE)
        self.do_click(self.PROFILE)
        time.sleep(1)
        self.do_click(self.PROFILEVALUE)
        self.do_click(self.LEVEL)
        time.sleep(1)
        self.do_click(self.LEVELVALUE)
        self.do_click(self.SCALE_G)
        time.sleep(1)
        self.do_click(self.SCALE_GVALUE)
        self.do_click(self.MUXRATE)
        time.sleep(1)
        self.do_click(self.MUXRATEVALUE)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
        
    
    def Add_vod_withsubtitle(self,profilename,logovderlay,identpath):
        time.sleep(2)
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        time.sleep(4)
        self.do_click(self.ADDNEW)
        self.do_click(self.TC)
        time.sleep(2)
        self.do_click(self.TCVALUE)
        self.do_send_keys(self.PROFILENAME,profilename)
        self.do_send_keys(self.LOGOOVERLAY,logovderlay)
        self.do_send_keys(self.IDENTPATH,identpath)
        self.do_click(self.OUTPUTEX)
        time.sleep(1)
        self.do_click(self.OUTPUTVALUE)
        self.do_click(self.PROFILE)
        time.sleep(1)
        self.do_click(self.PROFILEVALUE)
        self.do_click(self.LEVEL)
        time.sleep(1)
        self.do_click(self.LEVELVALUE)
        self.do_click(self.SCALE_G)
        time.sleep(1)
        self.do_click(self.SCALE_GVALUE)
        self.do_click(self.MUXRATE)
        time.sleep(1)
        self.do_click(self.MUXRATEVALUE)
        self.do_click(self.SUBTITLE)
        self.do_click(self.SUBTITLEVALUE)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE) 
        
    def Add_vod_withsubtitlepath(self,profilename,logovderlay,identpath,subtitalpath):
        time.sleep(2)
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        time.sleep(4)
        self.do_click(self.ADDNEW)
        self.do_click(self.TC)
        time.sleep(2)
        self.do_click(self.TCVALUE)
        self.do_send_keys(self.PROFILENAME,profilename)
        self.do_send_keys(self.LOGOOVERLAY,logovderlay)
        self.do_send_keys(self.IDENTPATH,identpath)
        self.do_click(self.OUTPUTEX)
        time.sleep(1)
        self.do_click(self.OUTPUTVALUE)
        self.do_click(self.PROFILE)
        time.sleep(1)
        self.do_click(self.PROFILEVALUE)
        self.do_click(self.LEVEL)
        time.sleep(1)
        self.do_click(self.LEVELVALUE)
        self.do_click(self.SCALE_G)
        time.sleep(1)
        self.do_click(self.SCALE_GVALUE)
        self.do_click(self.MUXRATE)
        time.sleep(1)
        self.do_click(self.MUXRATEVALUE)
        self.do_click(self.SUBTITLE)
        self.do_click(self.SUBTITLEVALUE)
        self.do_send_keys(self.SUBTITLEPATH,subtitalpath)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)  
           
    def Add_vod_withsubtitlelanguage(self,profilename,logovderlay,identpath,subtitalpath,subtilelanguage,remark):
        time.sleep(2)
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        time.sleep(4)
        self.do_click(self.ADDNEW)
        self.do_click(self.TC)
        time.sleep(2)
        self.do_click(self.TCVALUE)
        self.do_send_keys(self.PROFILENAME,profilename)
        self.do_send_keys(self.LOGOOVERLAY,logovderlay)
        self.do_send_keys(self.IDENTPATH,identpath)
        self.do_click(self.OUTPUTEX)
        time.sleep(1)
        self.do_click(self.OUTPUTVALUE)
        self.do_click(self.PROFILE)
        time.sleep(1)
        self.do_click(self.PROFILEVALUE)
        self.do_click(self.LEVEL)
        time.sleep(1)
        self.do_click(self.LEVELVALUE)
        self.do_click(self.SCALE_G)
        time.sleep(1)
        self.do_click(self.SCALE_GVALUE)
        self.do_click(self.MUXRATE)
        time.sleep(1)
        self.do_click(self.MUXRATEVALUE)
        self.do_click(self.SUBTITLE)
        self.do_click(self.SUBTITLEVALUE)
        self.do_send_keys(self.SUBTITLEPATH,subtitalpath)
        self.do_send_keys(self.SUBTITLEPATHLANGUAGE,subtilelanguage)
        self.do_send_keys(self.REMARK,remark)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
        
    def Add_vod_withpixelformet(self,profilename,logovderlay,identpath,subtitalpath,subtilelanguage,remark):
        time.sleep(2)
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        time.sleep(4)
        self.do_click(self.ADDNEW)
        self.do_click(self.TC)
        time.sleep(2)
        self.do_click(self.TCVALUE)
        self.do_send_keys(self.PROFILENAME,profilename)
        self.do_send_keys(self.LOGOOVERLAY,logovderlay)
        self.do_send_keys(self.IDENTPATH,identpath)
        self.do_click(self.OUTPUTEX)
        time.sleep(1)
        self.do_click(self.OUTPUTVALUE)
        self.do_click(self.PROFILE)
        time.sleep(1)
        self.do_click(self.PROFILEVALUE)
        self.do_click(self.LEVEL)
        time.sleep(1)
        self.do_click(self.LEVELVALUE)
        self.do_click(self.SCALE_G)
        time.sleep(1)
        self.do_click(self.SCALE_GVALUE)
        self.do_click(self.MUXRATE)
        time.sleep(1)
        self.do_click(self.MUXRATEVALUE)
        self.do_click(self.SUBTITLE)
        self.do_click(self.SUBTITLEVALUE)
        self.do_send_keys(self.SUBTITLEPATH,subtitalpath)
        self.do_send_keys(self.SUBTITLEPATHLANGUAGE,subtilelanguage)
        self.do_send_keys(self.REMARK,remark)
        self.do_click(self.AUDIOPARAMETERS)
        self.do_click(self.PICELFORMET)
        time.sleep(1)
        self.do_click(self.PICELFORMETVALUE)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
         
    def Add_vod_withsimplerate(self,profilename,logovderlay,identpath,subtitalpath,subtilelanguage,remark):
        time.sleep(2)
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        time.sleep(4)
        self.do_click(self.ADDNEW)
        self.do_click(self.TC)
        time.sleep(2)
        self.do_click(self.TCVALUE)
        self.do_send_keys(self.PROFILENAME,profilename)
        self.do_send_keys(self.LOGOOVERLAY,logovderlay)
        self.do_send_keys(self.IDENTPATH,identpath)
        self.do_click(self.OUTPUTEX)
        time.sleep(1)
        self.do_click(self.OUTPUTVALUE)
        self.do_click(self.PROFILE)
        time.sleep(1)
        self.do_click(self.PROFILEVALUE)
        self.do_click(self.LEVEL)
        time.sleep(1)
        self.do_click(self.LEVELVALUE)
        self.do_click(self.SCALE_G)
        time.sleep(1)
        self.do_click(self.SCALE_GVALUE)
        self.do_click(self.MUXRATE)
        time.sleep(1)
        self.do_click(self.MUXRATEVALUE)
        self.do_click(self.SUBTITLE)
        self.do_click(self.SUBTITLEVALUE)
        self.do_send_keys(self.SUBTITLEPATH,subtitalpath)
        self.do_send_keys(self.SUBTITLEPATHLANGUAGE,subtilelanguage)
        self.do_send_keys(self.REMARK,remark)
        self.do_click(self.AUDIOPARAMETERS)
        self.do_click(self.PICELFORMET)
        time.sleep(1)
        self.do_click(self.PICELFORMETVALUE)
        self.do_click(self.SIMPLERATE)
        self.do_click(self.SIMPLERATEVALUE)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
        
    def Add_vod_withaudiocodec(self,profilename,logovderlay,identpath,subtitalpath,subtilelanguage,remark):
        time.sleep(2)
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        time.sleep(4)
        self.do_click(self.ADDNEW)
        self.do_click(self.TC)
        time.sleep(2)
        self.do_click(self.TCVALUE)
        self.do_send_keys(self.PROFILENAME,profilename)
        self.do_send_keys(self.LOGOOVERLAY,logovderlay)
        self.do_send_keys(self.IDENTPATH,identpath)
        self.do_click(self.OUTPUTEX)
        time.sleep(1)
        self.do_click(self.OUTPUTVALUE)
        self.do_click(self.PROFILE)
        time.sleep(1)
        self.do_click(self.PROFILEVALUE)
        self.do_click(self.LEVEL)
        time.sleep(1)
        self.do_click(self.LEVELVALUE)
        self.do_click(self.SCALE_G)
        time.sleep(1)
        self.do_click(self.SCALE_GVALUE)
        self.do_click(self.MUXRATE)
        time.sleep(1)
        self.do_click(self.MUXRATEVALUE)
        self.do_click(self.SUBTITLE)
        self.do_click(self.SUBTITLEVALUE)
        self.do_send_keys(self.SUBTITLEPATH,subtitalpath)
        self.do_send_keys(self.SUBTITLEPATHLANGUAGE,subtilelanguage)
        self.do_send_keys(self.REMARK,remark)
        self.do_click(self.AUDIOPARAMETERS)
        self.do_click(self.PICELFORMET)
        time.sleep(1)
        self.do_click(self.PICELFORMETVALUE)
        self.do_click(self.SIMPLERATE)
        self.do_click(self.SIMPLERATEVALUE)
        self.do_click(self.AUDIOCODEC)
        self.do_click(self.AUDIOCODECVALUE)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
    
    def Add_vod_withaudiobitrate(self,profilename,logovderlay,identpath,subtitalpath,subtilelanguage,remark,audiobitrate):
        time.sleep(2)
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        time.sleep(4)
        self.do_click(self.ADDNEW)
        self.do_click(self.TC)
        time.sleep(2)
        self.do_click(self.TCVALUE)
        self.do_send_keys(self.PROFILENAME,profilename)
        self.do_send_keys(self.LOGOOVERLAY,logovderlay)
        self.do_send_keys(self.IDENTPATH,identpath)
        self.do_click(self.OUTPUTEX)
        time.sleep(1)
        self.do_click(self.OUTPUTVALUE)
        self.do_click(self.PROFILE)
        time.sleep(1)
        self.do_click(self.PROFILEVALUE)
        self.do_click(self.LEVEL)
        time.sleep(1)
        self.do_click(self.LEVELVALUE)
        self.do_click(self.SCALE_G)
        time.sleep(1)
        self.do_click(self.SCALE_GVALUE)
        self.do_click(self.MUXRATE)
        time.sleep(1)
        self.do_click(self.MUXRATEVALUE)
        self.do_click(self.SUBTITLE)
        self.do_click(self.SUBTITLEVALUE)
        self.do_send_keys(self.SUBTITLEPATH,subtitalpath)
        self.do_send_keys(self.SUBTITLEPATHLANGUAGE,subtilelanguage)
        self.do_send_keys(self.REMARK,remark)
        self.do_click(self.AUDIOPARAMETERS)
        self.do_click(self.PICELFORMET)
        time.sleep(1)
        self.do_click(self.PICELFORMETVALUE)
        self.do_click(self.SIMPLERATE)
        self.do_click(self.SIMPLERATEVALUE)
        self.do_click(self.AUDIOCODEC)
        self.do_click(self.AUDIOCODECVALUE)
        self.do_send_keys(self.AUDIOBITRATE,audiobitrate)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
        
    def Add_vod_withfreamrate(self,profilename,logovderlay,identpath,subtitalpath,subtilelanguage,remark,audiobitrate):
        time.sleep(2)
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        time.sleep(4)
        self.do_click(self.ADDNEW)
        self.do_click(self.TC)
        time.sleep(2)
        self.do_click(self.TCVALUE)
        self.do_send_keys(self.PROFILENAME,profilename)
        self.do_send_keys(self.LOGOOVERLAY,logovderlay)
        self.do_send_keys(self.IDENTPATH,identpath)
        self.do_click(self.OUTPUTEX)
        time.sleep(1)
        self.do_click(self.OUTPUTVALUE)
        self.do_click(self.PROFILE)
        time.sleep(1)
        self.do_click(self.PROFILEVALUE)
        self.do_click(self.LEVEL)
        time.sleep(1)
        self.do_click(self.LEVELVALUE)
        self.do_click(self.SCALE_G)
        time.sleep(1)
        self.do_click(self.SCALE_GVALUE)
        self.do_click(self.MUXRATE)
        time.sleep(1)
        self.do_click(self.MUXRATEVALUE)
        self.do_click(self.SUBTITLE)
        self.do_click(self.SUBTITLEVALUE)
        self.do_send_keys(self.SUBTITLEPATH,subtitalpath)
        self.do_send_keys(self.SUBTITLEPATHLANGUAGE,subtilelanguage)
        self.do_send_keys(self.REMARK,remark)
        self.do_click(self.AUDIOPARAMETERS)
        self.do_click(self.PICELFORMET)
        time.sleep(1)
        self.do_click(self.PICELFORMETVALUE)
        self.do_click(self.SIMPLERATE)
        self.do_click(self.SIMPLERATEVALUE)
        self.do_click(self.AUDIOCODEC)
        self.do_click(self.AUDIOCODECVALUE)
        self.do_send_keys(self.AUDIOBITRATE,audiobitrate)
        self.do_click(self.VIDEOPARAMETERS)
        self.do_click(self.FRAMERATE)
        self.do_click(self.FRAMERATEVALUE)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
        
    def Add_vod_withvideocodec(self,profilename,logovderlay,identpath,subtitalpath,subtilelanguage,remark,audiobitrate):
        time.sleep(2)
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        time.sleep(4)
        self.do_click(self.ADDNEW)
        self.do_click(self.TC)
        time.sleep(2)
        self.do_click(self.TCVALUE)
        self.do_send_keys(self.PROFILENAME,profilename)
        self.do_send_keys(self.LOGOOVERLAY,logovderlay)
        self.do_send_keys(self.IDENTPATH,identpath)
        self.do_click(self.OUTPUTEX)
        time.sleep(1)
        self.do_click(self.OUTPUTVALUE)
        self.do_click(self.PROFILE)
        time.sleep(1)
        self.do_click(self.PROFILEVALUE)
        self.do_click(self.LEVEL)
        time.sleep(1)
        self.do_click(self.LEVELVALUE)
        self.do_click(self.SCALE_G)
        time.sleep(1)
        self.do_click(self.SCALE_GVALUE)
        self.do_click(self.MUXRATE)
        time.sleep(1)
        self.do_click(self.MUXRATEVALUE)
        self.do_click(self.SUBTITLE)
        self.do_click(self.SUBTITLEVALUE)
        self.do_send_keys(self.SUBTITLEPATH,subtitalpath)
        self.do_send_keys(self.SUBTITLEPATHLANGUAGE,subtilelanguage)
        self.do_send_keys(self.REMARK,remark)
        self.do_click(self.AUDIOPARAMETERS)
        self.do_click(self.PICELFORMET)
        time.sleep(1)
        self.do_click(self.PICELFORMETVALUE)
        self.do_click(self.SIMPLERATE)
        self.do_click(self.SIMPLERATEVALUE)
        self.do_click(self.AUDIOCODEC)
        self.do_click(self.AUDIOCODECVALUE)
        self.do_send_keys(self.AUDIOBITRATE,audiobitrate)
        self.do_click(self.VIDEOPARAMETERS)
        self.do_click(self.FRAMERATE)
        self.do_click(self.FRAMERATEVALUE)
        self.do_click(self.VIDEOCODEC)
        self.do_click(self.VIDEOCODECVALUE)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
        
    def Add_vod_withresolution(self,profilename,logovderlay,identpath,subtitalpath,subtilelanguage,remark,audiobitrate,concatvideocodec):
        time.sleep(2)
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        time.sleep(4)
        self.do_click(self.ADDNEW)
        self.do_click(self.TC)
        time.sleep(2)
        self.do_click(self.TCVALUE)
        self.do_send_keys(self.PROFILENAME,profilename)
        self.do_send_keys(self.LOGOOVERLAY,logovderlay)
        self.do_send_keys(self.IDENTPATH,identpath)
        self.do_click(self.OUTPUTEX)
        time.sleep(1)
        self.do_click(self.OUTPUTVALUE)
        self.do_click(self.PROFILE)
        time.sleep(1)
        self.do_click(self.PROFILEVALUE)
        self.do_click(self.LEVEL)
        time.sleep(1)
        self.do_click(self.LEVELVALUE)
        self.do_click(self.SCALE_G)
        time.sleep(1)
        self.do_click(self.SCALE_GVALUE)
        self.do_click(self.MUXRATE)
        time.sleep(1)
        self.do_click(self.MUXRATEVALUE)
        self.do_click(self.SUBTITLE)
        self.do_click(self.SUBTITLEVALUE)
        self.do_send_keys(self.SUBTITLEPATH,subtitalpath)
        self.do_send_keys(self.SUBTITLEPATHLANGUAGE,subtilelanguage)
        self.do_send_keys(self.REMARK,remark)
        self.do_click(self.AUDIOPARAMETERS)
        self.do_click(self.PICELFORMET)
        time.sleep(1)
        self.do_click(self.PICELFORMETVALUE)
        self.do_click(self.SIMPLERATE)
        self.do_click(self.SIMPLERATEVALUE)
        self.do_click(self.AUDIOCODEC)
        self.do_click(self.AUDIOCODECVALUE)
        self.do_send_keys(self.AUDIOBITRATE,audiobitrate)
        self.do_click(self.VIDEOPARAMETERS)
        self.do_click(self.FRAMERATE)
        self.do_click(self.FRAMERATEVALUE)
        self.do_click(self.VIDEOCODEC)
        self.do_click(self.VIDEOCODECVALUE)
        self.do_click(self.RESOLUTION)
        self.do_click(self.RESOLUTIONVALUE)
        self.do_send_keys(self.CONCATVIDEOCODEC,concatvideocodec)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
        
    def Add_vod_withvideobitrate(self,profilename,logovderlay,identpath,subtitalpath,subtilelanguage,remark,audiobitrate,concatvideocodec,videobitrate):
        time.sleep(2)
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        time.sleep(4)
        self.do_click(self.ADDNEW)
        self.do_click(self.TC)
        time.sleep(2)
        self.do_click(self.TCVALUE)
        self.do_send_keys(self.PROFILENAME,profilename)
        self.do_send_keys(self.LOGOOVERLAY,logovderlay)
        self.do_send_keys(self.IDENTPATH,identpath)
        self.do_click(self.OUTPUTEX)
        time.sleep(1)
        self.do_click(self.OUTPUTVALUE)
        self.do_click(self.PROFILE)
        time.sleep(1)
        self.do_click(self.PROFILEVALUE)
        self.do_click(self.LEVEL)
        time.sleep(1)
        self.do_click(self.LEVELVALUE)
        self.do_click(self.SCALE_G)
        time.sleep(1)
        self.do_click(self.SCALE_GVALUE)
        self.do_click(self.MUXRATE)
        time.sleep(1)
        self.do_click(self.MUXRATEVALUE)
        self.do_click(self.SUBTITLE)
        self.do_click(self.SUBTITLEVALUE)
        self.do_send_keys(self.SUBTITLEPATH,subtitalpath)
        self.do_send_keys(self.SUBTITLEPATHLANGUAGE,subtilelanguage)
        self.do_send_keys(self.REMARK,remark)
        self.do_click(self.AUDIOPARAMETERS)
        self.do_click(self.PICELFORMET)
        time.sleep(1)
        self.do_click(self.PICELFORMETVALUE)
        self.do_click(self.SIMPLERATE)
        self.do_click(self.SIMPLERATEVALUE)
        self.do_click(self.AUDIOCODEC)
        self.do_click(self.AUDIOCODECVALUE)
        self.do_send_keys(self.AUDIOBITRATE,audiobitrate)
        self.do_click(self.VIDEOPARAMETERS)
        self.do_click(self.FRAMERATE)
        self.do_click(self.FRAMERATEVALUE)
        self.do_click(self.VIDEOCODEC)
        self.do_click(self.VIDEOCODECVALUE)
        self.do_click(self.RESOLUTION)
        self.do_click(self.RESOLUTIONVALUE)
        self.do_send_keys(self.CONCATVIDEOCODEC,concatvideocodec)
        self.do_send_keys(self.VIDEOBITRATE,videobitrate)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE) 
        
    def Add_vod_withminbitrate(self,profilename,logovderlay,identpath,subtitalpath,subtilelanguage,remark,audiobitrate,concatvideocodec,videobitrate,minbitrate):
        time.sleep(2)
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        time.sleep(4)
        self.do_click(self.ADDNEW)
        self.do_click(self.TC)
        time.sleep(2)
        self.do_click(self.TCVALUE)
        self.do_send_keys(self.PROFILENAME,profilename)
        self.do_send_keys(self.LOGOOVERLAY,logovderlay)
        self.do_send_keys(self.IDENTPATH,identpath)
        self.do_click(self.OUTPUTEX)
        time.sleep(1)
        self.do_click(self.OUTPUTVALUE)
        self.do_click(self.PROFILE)
        time.sleep(1)
        self.do_click(self.PROFILEVALUE)
        self.do_click(self.LEVEL)
        time.sleep(1)
        self.do_click(self.LEVELVALUE)
        self.do_click(self.SCALE_G)
        time.sleep(1)
        self.do_click(self.SCALE_GVALUE)
        self.do_click(self.MUXRATE)
        time.sleep(1)
        self.do_click(self.MUXRATEVALUE)
        self.do_click(self.SUBTITLE)
        self.do_click(self.SUBTITLEVALUE)
        self.do_send_keys(self.SUBTITLEPATH,subtitalpath)
        self.do_send_keys(self.SUBTITLEPATHLANGUAGE,subtilelanguage)
        self.do_send_keys(self.REMARK,remark)
        self.do_click(self.AUDIOPARAMETERS)
        self.do_click(self.PICELFORMET)
        time.sleep(1)
        self.do_click(self.PICELFORMETVALUE)
        self.do_click(self.SIMPLERATE)
        self.do_click(self.SIMPLERATEVALUE)
        self.do_click(self.AUDIOCODEC)
        self.do_click(self.AUDIOCODECVALUE)
        self.do_send_keys(self.AUDIOBITRATE,audiobitrate)
        self.do_click(self.VIDEOPARAMETERS)
        self.do_click(self.FRAMERATE)
        self.do_click(self.FRAMERATEVALUE)
        self.do_click(self.VIDEOCODEC)
        self.do_click(self.VIDEOCODECVALUE)
        self.do_click(self.RESOLUTION)
        self.do_click(self.RESOLUTIONVALUE)
        self.do_send_keys(self.CONCATVIDEOCODEC,concatvideocodec)
        self.do_send_keys(self.VIDEOBITRATE,videobitrate)
        self.do_send_keys(self.MINBITRATE,minbitrate)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
        
    
    def Add_vod_save(self,profilename,logovderlay,identpath,subtitalpath,subtilelanguage,remark,audiobitrate,concatvideocodec,videobitrate,minbitrate,maxbitrate,extraparameter):
        time.sleep(2)
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        time.sleep(4)
        self.do_click(self.ADDNEW)
        self.do_click(self.TC)
        time.sleep(2)
        self.do_click(self.TCVALUE)
        self.do_send_keys(self.PROFILENAME,profilename)
        self.do_send_keys(self.LOGOOVERLAY,logovderlay)
        self.do_send_keys(self.IDENTPATH,identpath)
        self.do_click(self.OUTPUTEX)
        time.sleep(1)
        self.do_click(self.OUTPUTVALUE)
        self.do_click(self.PROFILE)
        time.sleep(1)
        self.do_click(self.PROFILEVALUE)
        self.do_click(self.LEVEL)
        time.sleep(1)
        self.do_click(self.LEVELVALUE)
        self.do_click(self.SCALE_G)
        time.sleep(1)
        self.do_click(self.SCALE_GVALUE)
        self.do_click(self.MUXRATE)
        time.sleep(1)
        self.do_click(self.MUXRATEVALUE)
        self.do_click(self.SUBTITLE)
        self.do_click(self.SUBTITLEVALUE)
        self.do_send_keys(self.SUBTITLEPATH,subtitalpath)
        self.do_send_keys(self.SUBTITLEPATHLANGUAGE,subtilelanguage)
        self.do_send_keys(self.REMARK,remark)
        self.do_click(self.AUDIOPARAMETERS)
        self.do_click(self.PICELFORMET)
        time.sleep(1)
        self.do_click(self.PICELFORMETVALUE)
        self.do_click(self.SIMPLERATE)
        self.do_click(self.SIMPLERATEVALUE)
        self.do_click(self.AUDIOCODEC)
        self.do_click(self.AUDIOCODECVALUE)
        self.do_send_keys(self.AUDIOBITRATE,audiobitrate)
        self.do_click(self.VIDEOPARAMETERS)
        self.do_click(self.FRAMERATE)
        self.do_click(self.FRAMERATEVALUE)
        self.do_click(self.VIDEOCODEC)
        self.do_click(self.VIDEOCODECVALUE)
        self.do_click(self.RESOLUTION)
        self.do_click(self.RESOLUTIONVALUE)
        self.do_send_keys(self.CONCATVIDEOCODEC,concatvideocodec)
        self.do_send_keys(self.VIDEOBITRATE,videobitrate)
        self.do_send_keys(self.MINBITRATE,minbitrate)
        self.do_send_keys(self.MAXBITRATE,maxbitrate)
        self.do_click(self.OTHER)
        self.do_send_keys(self.EXTRAPARAMETER,extraparameter)
        self.do_click(self.SAVEBUTTON)
        if self.is_visible(self.ALERT_MESSAGE):
            return self.get_element_text(self.ALERT_MESSAGE)
      
    def update_data(self,profilename):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        time.sleep(5)
        if self.is_visible(self.UPDATEDATA):
            time.sleep(5)
            if(self.get_element_text(self.UPDATEDATA)=="automationtesting"):
                # time.sleep(5)
                self.do_click(self.UPDATEDATA)
                # time.sleep(5)
                self.do_send_keys(self.LOGOOVERLAY,profilename)
                # time.sleep(5)
                self.do_click(self.SAVEBUTTON)
                time.sleep(1)
                if(self.get_element_text(self.UPDATEDATA_NEW)=="automationtesting"):
                    if self.is_visible(self.ALERT_MESSAGE):
                        return self.get_element_text(self.ALERT_MESSAGE)
                        #time.sleep(5)        

    def delete_data(self):
        self.do_click(self.PROFILEBUTTON)
        self.do_click(self.VODBUTTON)
        if self.is_visible(self.UPDATEDATA_NEW):
            if(self.get_element_text(self.UPDATEDATA_NEW)=="automationtesting"):
                time.sleep(5)
                self.do_click(self.DELETEBUTTON)
                self.do_click(self.YESBUTTON)
                if self.is_visible(self.ALERT_MESSAGE):
                    return self.get_element_text(self.ALERT_MESSAGE)