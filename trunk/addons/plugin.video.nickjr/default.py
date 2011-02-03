import urllib,urllib2,re,sys,xbmcplugin,xbmcgui,xbmcaddon
pluginhandle = int(sys.argv[1])

def CATS():
        addDir('Videos','http://www.nickjr.com/common/data/kids/get-kids-config-data.jhtml?fsd=/dynaboss&urlAlias=kids-video-landing',1,'','')
        addDir('Channels','http://www.nickjr.com/video/index.jhtml',2,'','')

def SHOWS(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link = page.read()
        names = re.compile('"title":"(.+?)"').findall(link)
        thumbs = re.compile('"thumbnail":"(.+?)"').findall(link)
        urls = re.compile('"link":"(.+?)"').findall(link)
	videos = [(names[i],thumbs[i],urls[i])for i in range (0,len(thumbs))]
	for name,thumb,url in videos:
		addDir(name.replace('&amp;','&'),'http://www.nickjr.com'+url,3,'http://www.nickjr.com/'+thumb,'')

def CHANNELS(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link = page.read()
        all=re.compile('<span>Channels</span>.+?<span>Shows</span>', re.DOTALL).findall(link)
	match=re.compile('<a href=".+?id=(.+?)" id=".+?">(.+?)</a>').findall(all[0])	
	for url,name in match:
		addDir(name.replace('&amp;','&'),'http://www.nickjr.com/dynamo/video/data/mrssGen.jhtml?type=network&loc=sidebar&hub=njParentsHub&mode=playlist&mgid=mgid:cms:item:nickjr.com:'+url,4,'','')

def SUBSHOWS(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link = page.read()
        urlalias = re.compile('"urlAlias", "(.+?)"').findall(link)[0]
        req = urllib2.Request('http://www.nickjr.com/common/data/kids/get-kids-config-data.jhtml?fsd=/dynaboss&urlAlias='+urlalias)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link = page.read()
        names = re.compile('"title":"(.+?)"').findall(link)
        thumbs = re.compile('"thumbnail":"(.+?)"').findall(link)
        urls = re.compile('"id":"(.+?)"').findall(link)
	videos = [(names[i],thumbs[i],urls[i])for i in range (0,len(thumbs))]
	for name,thumb,url in videos:
	        u=sys.argv[0]+"?url="+urllib.quote_plus('http://www.nickjr.com/dynamo/video/data/mediaGen.jhtml?mgid=mgid:cms:item:nickjr.com:'+url+'&block=false',name)+"&mode="+str(5)
                item=xbmcgui.ListItem(name.replace('&amp;','&'), thumbnailImage=thumb)
          	item.setInfo( type="Video", infoLabels={ "Title": name} )                
		item.setProperty('IsPlayable', 'true')
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)

def SUBCHANNELS(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link = page.read()
        names = re.compile('<media:title>(.+?)</media:title>').findall(link)
        urls = re.compile('<media:player url="http://media.mtvnservices.com/mgid:cms:item:nickjr.com:(.+?)"/>').findall(link)
	videos = [(names[i],urls[i])for i in range (0,len(names))]
	for name,url in videos:
	        u=sys.argv[0]+"?url="+urllib.quote_plus('http://www.nickjr.com/dynamo/video/data/mediaGen.jhtml?mgid=mgid:cms:item:nickjr.com:'+url+'&block=false',name)+"&mode="+str(5)
                item=xbmcgui.ListItem(name.replace('&amp;','&'))
          	item.setInfo( type="Video", infoLabels={ "Title": name} )                
		item.setProperty('IsPlayable', 'true')
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)


def PLAY(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link=page.read()
	finalurl=re.compile('src>(.+?)</src>').findall(link)[0]
     	item = xbmcgui.ListItem(path=finalurl)
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
        SHOWS(url)
elif mode==2:
        print "PAGE"
        CHANNELS(url)
elif mode==3:
        print "PAGE"
        SUBSHOWS(url)
elif mode==4:
        print "PAGE"
        SUBCHANNELS(url)
elif mode==5:
        print "PAGE"
        PLAY(url)
elif mode==6:
        print "SEARCH  :"+url
        SEARCH()
        
xbmcplugin.endOfDirectory(int(sys.argv[1]))