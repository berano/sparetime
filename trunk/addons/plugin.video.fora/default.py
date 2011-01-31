import urllib,urllib2,re,sys,xbmcplugin,xbmcgui,xbmcaddon

def CATS():
        addDir('Economy','http://fora.tv/topic/economy',1,'','')
        addDir('Environment','http://fora.tv/topic/environment',2,'','')
        addDir('Politics','http://fora.tv/topic/politics',3,'','')
        addDir('Science','http://fora.tv/topic/science',4,'','')
        addDir('Technology','http://fora.tv/topic/technology',5,'','')
        addDir('Culture','http://fora.tv/topic/culture',6,'','')
        addDir('Featured Programs','http://fora.tv/',11,'','')
        addDir('Search','http://fora.tv/',13,'','')

def EC(url):
        addDir('Featured Programs on Economy','http://fora.tv/topic/economy',7,'','')
        addDir('This Week Most Watched','http://fora.tv/topic/economy',8,'','')
        addDir('Recently Featured in Economy','http://fora.tv/topic/economy',9,'','')
        addDir('All Programs in Economy','http://fora.tv/topic/economy/all',10,'','')

def EN(url):
        addDir('Featured Programs on environment','http://fora.tv/topic/environment',7,'','')
        addDir('This Week Most Watched','http://fora.tv/topic/environment',8,'','')
        addDir('Recently featured in environment','http://fora.tv/topic/environment',9,'','')
        addDir('All Programs in Environment','http://fora.tv/topic/environment/all',10,'','')

def PL(url):
        addDir('Featured Programs on politics','http://fora.tv/topic/politics',7,'','')
        addDir('This Week Most Watched','http://fora.tv/topic/politics',8,'','')
        addDir('Recently featured in politics','http://fora.tv/topic/politics',9,'','')
        addDir('All Programs in Politics','http://fora.tv/topic/politics/all',10,'','')

def SC(url):
        addDir('Featured Programs on science','http://fora.tv/topic/science',7,'','')
        addDir('This Week Most Watched','http://fora.tv/topic/science',8,'','')
        addDir('Recently featured in science','http://fora.tv/topic/science',9,'','')
        addDir('All Programs in Science','http://fora.tv/topic/science/all',10,'','')

def TC(url):
        addDir('Featured Programs on technology','http://fora.tv/topic/technology',7,'','')
        addDir('This Week Most Watched','http://fora.tv/topic/technology',8,'','')
        addDir('Recently featured in technology','http://fora.tv/topic/technology',9,'','')
        addDir('All Programs in Technology','http://fora.tv/topic/technology/all',10,'','')

def CT(url):
        addDir('Featured Programs on culture','http://fora.tv/topic/culture',7,'','')
        addDir('This Week Most Watched','http://fora.tv/topic/culture',8,'','')
        addDir('Recently featured in culture','http://fora.tv/topic/culture',9,'','')
        addDir('All Programs in Culture','http://fora.tv/topic/culture/all',10,'','')

def FEAT1(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link=page.read()
	match=re.compile('href="(.+?)"><img src="(.+?)" width=.+? height=.+? alt="(.+?)"').findall(link)
	for url,thumb,name in match:
	        u=sys.argv[0]+"?url="+urllib.quote_plus("http://fora.tv"+url,name)+"&mode="+str(12)
                item=xbmcgui.ListItem(name, iconImage="http://fora.tv"+thumb)
          	item.setInfo( type="Video", infoLabels={ "Title": name} )                
		item.setProperty('IsPlayable', 'true')
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)
def MOSTW(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link=page.read()
	match=re.compile('<dt>.+?</dt><dd><a href="(.+?)">(.+?)</a></dd>').findall(link)
	for url,name in match:
	        u=sys.argv[0]+"?url="+urllib.quote_plus("http://fora.tv"+url,name)+"&mode="+str(12)
                item=xbmcgui.ListItem(name, iconImage="http://fora.tv")
          	item.setInfo( type="Video", infoLabels={ "Title": name} )                
		item.setProperty('IsPlayable', 'true')
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)
def RECC(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link=page.read()
	match=re.compile('<a class="cropped_thumb" href="(.+?)"><img src="(.+?)" width=.+? height=.+? alt="(.+?)"').findall(link)
	for url,thumb,name in match:
	        u=sys.argv[0]+"?url="+urllib.quote_plus("http://fora.tv"+url,name)+"&mode="+str(12)
                item=xbmcgui.ListItem(name, iconImage="http://fora.tv"+thumb)
          	item.setInfo( type="Video", infoLabels={ "Title": name} )                
		item.setProperty('IsPlayable', 'true')
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)
def FEAT(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link=page.read()
	code=re.compile('form method="GET" action="(.+?)"').findall(link)[0]
	thumbs=re.compile('background-image:url.(.+?).;').findall(link)
        urls=re.compile('<div class="featured_title">\n          <a href="(.+?)">.+?</a>').findall(link)
        names=re.compile('<div class="featured_title">\n          <a href=".+?">(.+?)</a>').findall(link)
	matchsearch=re.compile('<a class="cropped_thumb" href="(.+?)"><img src="(.+?)" width=.+? height=.+? alt="" /></a>\n.+?<a class=".+?" href=".+?">(.+?)</a>').findall(link)
	nxt=re.compile('    <li><a  href="(.+?)">Next</a></li>').findall(link)
	videos=[(names[i],urls[i],thumbs[i])for i in range (0,len(urls))]
	for url in nxt:
		addDir(' Next',"http://fora.tv"+code+url,10,'','')
	for name,url,thumb in videos:
	        u=sys.argv[0]+"?url="+urllib.quote_plus("http://fora.tv"+url,name)+"&mode="+str(12)
                item=xbmcgui.ListItem(name, iconImage="http://fora.tv"+thumb.replace('(','').replace(')','').replace(';',''))
          	item.setInfo( type="Video", infoLabels={ "Title": name} )                
		item.setProperty('IsPlayable', 'true')
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)

	for url,thumb,name in matchsearch:
	        u=sys.argv[0]+"?url="+urllib.quote_plus("http://fora.tv"+url,name)+"&mode="+str(12)
                item=xbmcgui.ListItem(name, iconImage="http://fora.tv"+thumb)
          	item.setInfo( type="Video", infoLabels={ "Title": name} )                
		item.setProperty('IsPlayable', 'true')
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)

def LIST(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link=page.read()
	match=re.compile('            <a class="cropped_image" href="(.+?)"><img src="(.+?)" width=.+? height=.+? alt="(.+?)" /></a>\n            <div class="featured_content">').findall(link)
	for url,thumb,name in match:
	        u=sys.argv[0]+"?url="+urllib.quote_plus("http://fora.tv"+url,name)+"&mode="+str(12)
                item=xbmcgui.ListItem(name, iconImage="http://fora.tv"+thumb)
          	item.setInfo( type="Video", infoLabels={ "Title": name} )                
		item.setProperty('IsPlayable', 'true')
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)

def PLAY(url,name):
	req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link=page.read()
	cid=re.compile('var full_program_clipid = (.+?);').findall(link)
	codecid = cid[0]
        req = urllib2.Request("http://fora.tv/fora/fora_player_full?cid="+codecid+"&h=0&b=0&p=FORA_Player_5&r=Other/Unrecognized")
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        page = urllib2.urlopen(req)
	link2=page.read()
	cod=re.compile('<encode_url>(.+?)</encode_url>').findall(link2)[0]
	if ".flv" in cod:
		code= cod.replace('.flv','')
	    	finalurl = "rtmp://foratv.fcod.llnwd.net/a953/o10/"+code
            	item = xbmcgui.ListItem(path=finalurl)
            	xbmcplugin.setResolvedUrl(pluginhandle, True, item)
		return
	dialog = xbmcgui.Dialog()
	ok = dialog.ok('FORA.tv', 'Error: Video unsupported')
	return ok

pluginhandle = int (sys.argv[1])

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
        keyb = xbmc.Keyboard('', 'Search FORA.TV')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
                req = urllib2.Request('http://fora.tv/search_video?q='+encode)
	        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        	page = urllib2.urlopen(req)
		link=page.read()
		match=re.compile('<a class="cropped_thumb" href="(.+?)"><img src="(.+?)" width=.+? height=.+? alt="" /></a>\n.+?<a class=".+?" href=".+?">(.+?)</a>').findall(link)
		nxt=re.compile('<li><a  href="(.+?)>Next</a></li>').findall(link)
		for url,thumb,name in match:
			addDir(name,"http://fora.tv"+url,12,"http://fora.tv"+thumb)
		for url in nxt:
			addDir(' Next',"http://fora.tv/search_video"+url,10,'')

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
        EC(url)
elif mode==2:
        print "PAGE"
        EN(url)
elif mode==3:
        print "PAGE"
        PL(url)
elif mode==4:
        print "PAGE"
        SC(url)
elif mode==5:
        print "PAGE"
        TC(url)
elif mode==6:
        print "PAGE"
        CT(url)
elif mode==7:
        print "PAGE"
        FEAT1(url)
elif mode==8:
        print "PAGE"
        MOSTW(url)
elif mode==9:
        print "PAGE"
        RECC(url)
elif mode==10:
        print "PAGE"
        FEAT(url)
elif mode==11:
        print "PAGE"
        LIST(url)
elif mode==12:
        print "PAGE"
        PLAY(url,name)
elif mode==13:
        print "SEARCH  :"+url
        SEARCH()
        
xbmcplugin.endOfDirectory(int(sys.argv[1]))