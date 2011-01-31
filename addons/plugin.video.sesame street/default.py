import urllib,urllib2,re,sys,xbmcplugin,xbmcgui,xbmcaddon
pluginhandle = int(sys.argv[1])

def CATS():
        addDir('Videos','http://www.sesamestreet.org/browseallvideos',1,'','')
        addDir('Sesame Playlists','http://www.sesamestreet.org/browseallplaylists',2,'','')
        addDir('Search','http://www.sesamestreet.org/',8,'','')

def VIDS(url):
        addDir('Browse All','http://www.sesamestreet.org/browseallvideos',4,'','')
        addDir('By Subject','http://www.sesamestreet.org/browsevideosbysubject',3,'','')
        addDir('By Theme','http://www.sesamestreet.org/browsevideosbytheme',3,'','')
        addDir('By Character','http://www.sesamestreet.org/browsevideosbycharacter',3,'','')
        addDir('Songs','http://www.sesamestreet.org/browseallvideos?p_p_id=browsegpv_WAR_browsegpvportlet&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_count=1&_browsegpv_WAR_browsegpvportlet_assetType=SONG',4,'','')
	addDir('Classic Clips','http://www.sesamestreet.org/browseallvideos?p_p_id=browsegpv_WAR_browsegpvportlet&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&p_p_col_id=column-2&p_p_col_count=1&_browsegpv_WAR_browsegpvportlet_assetType=CLASSIC',4,'','')

def PLISTS(url):
        addDir('Browse All','http://www.sesamestreet.org/browseallplaylists',10,'','')
        addDir('By Subject','http://www.sesamestreet.org/browseplaylistsbysubject',9,'','')
        addDir('By Theme','http://www.sesamestreet.org/browseplaylistsbytheme',9,'','')
        addDir('By Character','http://www.sesamestreet.org/browseplaylistsbycharacter',9,'','')

def SCRAP1(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link=page.read()
        all=re.compile('<!-- Start Rounded Container Here -->.+?<!-- End Rounded Container Here -->', re.DOTALL).findall(link)
	match=re.compile('href="(.+?)" class=".+?"><span>(.+?)</span></a>').findall(all[0])
	for url,name in match:
		addDir(name,url,4,'','')

def SCRAP2(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link=page.read()
        all=re.compile('<span>List View</span>.+?<div class="container-footer">', re.DOTALL).findall(link)
	match=re.compile('href="(.+?)" target="_self">	<img src="(.+?)" alt="" width="120" height="90" border="0" /><span class=".+?"></span>	</a>	</div></div><div class="text">.+?="title">	<a href=".+?" target="_self"><span>(.+?)</span>').findall(all[0])
        nxt=re.compile('class="button more" href="(.+?)">').findall(link)
	for url,thumb,name in match:
	        u=sys.argv[0]+"?url="+urllib.quote_plus(url,name)+"&mode="+str(5)
                item=xbmcgui.ListItem(name, thumbnailImage='http://www.sesamestreet.org/'+thumb)
          	item.setInfo( type="Video", infoLabels={ "Title": name} )                
		item.setProperty('IsPlayable', 'true')
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)
	for url in nxt:
		addDir('More',url,4,'','')

def SCRAP3(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link=page.read()
        all=re.compile('<!-- Start Rounded Container Here -->.+?<!-- End Rounded Container Here -->', re.DOTALL).findall(link)
	match=re.compile('href="(.+?)" class=".+?"><span>(.+?)</span></a>').findall(all[0])
	for url,name in match:
		addDir(name,url,10,'','')

def SCRAP4(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link=page.read()
        all=re.compile('<span>List View</span>.+?<div class="container-footer">', re.DOTALL).findall(link)
	match=re.compile('href="(.+?)" target="_self">	<img src="(.+?)" alt="" width="120" height="90" border="0" /><span class=".+?"></span>	</a>	</div></div><div class="text">.+?="title">	<a href=".+?" target="_self"><span>(.+?)</span>').findall(all[0])
        nxt=re.compile('class="button more" href="(.+?)">').findall(link)
	for url,thumb,name in match:
	        u=sys.argv[0]+"?url="+urllib.quote_plus(url,name)+"&mode="+str(6)
                item=xbmcgui.ListItem(name, thumbnailImage='http://www.sesamestreet.org/'+thumb)
          	item.setInfo( type="Video", infoLabels={ "Title": name} )                
		item.setProperty('IsPlayable', 'true')
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)
	for url in nxt:
		addDir('More',url,10,'','')

def SEARCHURL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link=page.read()
        all=re.compile('<span>List View</span>.+?<div class="container-footer">', re.DOTALL).findall(link)
	match=re.compile('<a href="(.+?)" ><div class="search-title">(.+?)</div></a>').findall(link)
	nxt=re.compile('<a href="(.+?)" class="button more"><span>Next</span>').findall(link)
	for url,name in match:
	        u=sys.argv[0]+"?url="+urllib.quote_plus("http://www.sesamestreet.org"+url,name)+"&mode="+str(5)
                item=xbmcgui.ListItem(name)
          	item.setInfo( type="Video", infoLabels={ "Title": name} )                
		item.setProperty('IsPlayable', 'true')
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)
	for url in nxt:
		addDir('More',url,7,'','')

def PLAYSINGLE(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link=page.read()
	code=re.compile('videoQueueBrowseAll&uid=(.+?)"').findall(link)[0]
        req = urllib2.Request('http://www.sesamestreet.org/cms_services/services?action=player&type=videoQueueBrowseAll&uid='+code)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link2=page.read()
        stacked_url = 'stack://'
	code2=re.compile('<filename><.+?CDATA.+?(.+?)]]></filename>').findall(link2)[:1]
	for url in code2:
	        stacked_url += url+' , '
        stacked_url2 = stacked_url[:-3]
	print stacked_url
     	item = xbmcgui.ListItem(path=stacked_url2)
        xbmcplugin.setResolvedUrl(pluginhandle, True, item)

def PLAYLIST(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link=page.read()
	code=re.compile('type=playlist&uid=(.+?)"').findall(link)[0]
        req = urllib2.Request('http://www.sesamestreet.org/cms_services/services?action=player&type=playlist&uid='+code)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link2=page.read()
        stacked_url = 'stack://'
	code2=re.compile('<filename><.+?CDATA.+?rtmp(.+?)]]></filename>').findall(link2)
	for url in code2:
	        stacked_url += 'rtmp'+ url +' , '
        stacked_url2 = stacked_url[:-3]
	print stacked_url
     	item = xbmcgui.ListItem(path=stacked_url2)
        xbmcplugin.setResolvedUrl(pluginhandle, True, item)

		
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
        return param

def SEARCH():
        keyb = xbmc.Keyboard('', 'Search Sesame')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
                req = urllib2.Request('http://www.sesamestreet.org/globalsearch?p_p_id=search_WAR_searchportlet&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_search_WAR_searchportlet_javax.portlet.action=search&_search_WAR_searchportlet_keywords='+encode+'&_search_WAR_searchportlet_type=VIDEO')
	        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        	page = urllib2.urlopen(req)
		link=page.read()
		match=re.compile('<a href="(.+?)" ><div class="search-title">(.+?)</div></a>').findall(link)
		nxt=re.compile('<a href="(.+?)" class="button more"><span>Next</span>').findall(link)
		for url,name in match:
	        	u=sys.argv[0]+"?url="+urllib.quote_plus("http://www.sesamestreet.org"+url,name)+"&mode="+str(5)
                	item=xbmcgui.ListItem(name)
          		item.setInfo( type="Video", infoLabels={ "Title": name} )                
			item.setProperty('IsPlayable', 'true')
                	xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)
		for url in nxt:
			addDir(' Next',url,7,'')

def addDir(name,url,mode,thumbnail,plot=''):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=thumbnail)
        liz.setInfo( type="Video", infoLabels={ "Title": name,
                                                "plot": plot} )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

      
def addLink(name,url,iconimage,plot,date):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        liz.setInfo( type="Video", infoLabels={ "Plot": plot} )
        liz.setInfo( type="Video", infoLabels={ "Date": date} )
	liz.setProperty("IsPlayable","true");
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        return ok

params=get_params()
url=None
name=None
mode=None
try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
if mode==None or url==None or len(url)<1:
        print "categories"
        CATS()
elif mode==1:
        print "PAGE"
        VIDS(url)
elif mode==2:
        print "PAGE"
        PLISTS(url)
elif mode==3:
        print "PAGE"
        SCRAP1(url)
elif mode==4:
        print "PAGE"
        SCRAP2(url)
elif mode==9:
        print "PAGE"
        SCRAP3(url)
elif mode==10:
        print "PAGE"
        SCRAP4(url)
elif mode==5:
        print "PAGE"
        PLAYSINGLE(url)
elif mode==6:
        print "PAGE"
        PLAYLIST(url)
elif mode==7:
        print "PAGE"
        SEARCHURL(url)
elif mode==8:
        print "SEARCH  :"+url
        SEARCH()
        
xbmcplugin.endOfDirectory(int(sys.argv[1]))