import urllib,urllib2,re,sys,xbmcplugin,xbmcgui,xbmcaddon,httplib,os
pluginhandle = int(sys.argv[1])

settings={}
settings['proxy'] = xbmcplugin.getSetting(pluginhandle,'us_proxy_enable')

def CATS():
	addDir('Popular TV Shows','http://www.mtv.com/',9,'')
	addDir('All Current MTV Shows','http://www.mtv.com/ontv/all/current.jhtml',1,'')
	addDir('Archives of MTV Shows','http://www.mtv.com/ontv/all/index.jhtml',7,'')
	addLink('name','rtmpe://viacom.fcod.llnwd.net/a3951/e15/gsp.nickcomstor/nickvision/nick/onair/shows/icarly/ni_icarly_rt227177_307_cart_a_640x480_1600.mp4','','','')
 
def LISTING(url):
	req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        all = re.compile('<span>Current MTV Shows</span>.+?<div class="group-a">', re.DOTALL).findall(link)
        urls = re.compile('a href="/shows(.+?)">').findall(all[0])
        thumbs = re.compile('src="/onair(.+?)"').findall(all[0])
        names = re.compile('alt="(.+?)"').findall(all[0])
	next = re.compile('<a class="page-next" href="(.+?)"').findall(link)
	videos = [(names[i],urls[i],thumbs[i])for i in range (0,len(names))]
	for name,url,thumb in videos:
		addDir(name,'http://www.mtv.com/shows'+url,2,'http://www.mtv.com/onair'+thumb,'')
	addDir('I Used To Be Fat','http://www.mtv.com/shows/i_used_to_be_fat/series.jhtml',2,'http://www.mtv.com/onair/i_used_to_be_fat/images/seriesmain/140x105.jpg','')
	for url in next:
		addDir(' More','http://www.mtv.com'+url,1,'','')

def LISTING2(url):
	req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        all = re.compile('<h1 class="h-main group">.+?<div class="group-a">', re.DOTALL).findall(link)
        urls = re.compile('a href="(.+?)">').findall(all[0])
        thumbs = re.compile('src="(.+?)"').findall(all[0])
        names = re.compile('alt="(.+?)"').findall(all[0])
	next = re.compile('<a class="page-next" href="(.+?)"').findall(link)
	videos = [(names[i],urls[i],thumbs[i])for i in range (0,len(names))]
	for name,url,thumb in videos:
		addDir(name,'http://www.mtv.com'+url,2,'http://www.mtv.com'+thumb,'')
	for url in next:
		addDir(' More','http://www.mtv.com'+url,7,'','')

def LISTINGPOPULAR(url):
	req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        all = re.compile('<span>Popular Shows</span>.+?<a href="/ontv/all/" class=" allshows">', re.DOTALL).findall(link)
        urls = re.compile('<a href="(.+?)">(.+?)</a>').findall(all[0])
	for url,name in urls:
		addDir(name,'http://www.mtv.com'+url,2,'','')

def EP_CP(name,url):
	req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
	changeurl = response.geturl()
	if '</b>Full Episodes</a>' in link:
		addDir('Full Episodes',changeurl.replace('series.jhtml','video.jhtml?filter=fulleps'),3,'','')
	if '</b>Bonus Clips</a>' in link:
		addDir('Bonus Clips',changeurl.replace('series.jhtml','video.jhtml?filter=bonusclips'),4,'','')
	if '</b>After Shows</a>' in link:
		addDir('After Shows',changeurl.replace('series.jhtml','video.jhtml?filter=aftershows'),4,'','')
	if '</b>Recaps</a>' in link:
		addDir('Recaps',changeurl.replace('series.jhtml','video.jhtml?filter=recaps'),4,'','')
	if '</b>Sneak Peeks</a>' in link:
		addDir('Sneak Peeks',changeurl.replace('series.jhtml','video.jhtml?filter=sneakpeeks'),4,'','')
	if '>Watch Video</a>' in link:
		addDir('Watch Video',changeurl.replace('series.jhtml','video.jhtml'),4,'','')


def EPISODES(url):
	req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
       	all = re.compile('<ol class="vidlist list-header">.+?<li class="last">', re.DOTALL).findall(link)
	try:
        	names = re.compile('maintitle="(.+?)"').findall(all[0])
	except:
		dialog = xbmcgui.Dialog()
		ok = dialog.ok("MTV Shows",'Sorry, there is no full episodes')
		return
        thumbs = re.compile('src="(.+?)"').findall(all[0])
        urls = re.compile('mainuri="mgid:uma:videolist:mtv.com:(.+?)"').findall(all[0])
	dates = re.compile('mainposted="(.+?)"').findall(all[0])
	videos = [(names[i],urls[i],thumbs[i],dates[i])for i in range (0,len(urls))]
	for name,url,thumb,date in videos:
		addDir(name,'http://www.mtv.com/player/embed/AS3/fullepisode/rss/?id='+url+'&uri=mgid:uma:videolist:mtv.com:'+url+'&instance= fullepisode'+url,6,'http://www.mtv.com'+thumb,date)

def CLIPS(name,url):
	req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
	series = re.compile('mainurl="/videos/?series=(.+?)&amp.+?"').findall(link)
	try:
		seriesID = re.compile('mainurl=".+?seriesId=(.+?)&amp.+?"').findall(link)[0]
	except:
		dialog = xbmcgui.Dialog()
		ok = dialog.ok("MTV Shows",'Sorry, there is no bonus clips')
		return
       	all = re.compile('<ol class="vidlist list-header">.+?<li class="last">', re.DOTALL).findall(link)
        names = re.compile('maintitle="(.+?)"').findall(all[0])
        thumbs = re.compile('src="(.+?)"').findall(all[0])
        urls = re.compile('mainurl=".+?id=(.+?)"').findall(all[0])
	videos = [(names[i],urls[i],thumbs[i])for i in range (0,len(urls))]
	for name,url,thumb in videos:
	        u=sys.argv[0]+"?url="+urllib.quote_plus('http://www.mtv.com/global/music/videos/ajax/playlist.jhtml?id='+url+'&seriesID='+seriesID)+"&mode="+str(5)
                item=xbmcgui.ListItem(name, thumbnailImage='http://www.mtv.com'+thumb)
          	item.setInfo( type="Video", infoLabels={ "Title": name} )                
		item.setProperty('IsPlayable', 'true')
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)

def PLAYCLIP(name,url):
	req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
	realink = re.compile('<a href="(.+?)">').findall(link)[0]
	req = urllib2.Request('http://wwww.mtv.com'+realink)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
	id1 = re.compile('MTVN.Player.vid = (.+?);').findall(link)[0]
	id2 = re.compile('MTVN.Player.defaultPlaylistId = (.+?);').findall(link)[0]
	url = 'http://www.mtv.com/player/includes/mediaGen.jhtml?uri=mgid:uma:video:mtv.com:'+id1+'&id='+id2+'&vid='+id1+'&ref=www.mtv.com&viewUri=mgid:uma:video:mtv.com:'+id1
	if (settings['proxy'] == 'true'):
        	link= proxy(url,True)
        else:
                link= proxy(url)

	if 'mtvnorigin' in link:
		clean = re.compile('rtmpe://cp10740.edgefcs.net/ondemand/mtvnorigin/gsp.egvrenditions/mtv.com/(.+?).mp4').findall(link)[-1]
		finalurl = "rtmpe://cp10740.edgefcs.net/ondemand/" + " playpath=mp4:mtvnorigin/gsp.egvrenditions/mtv.com/"+ clean + " swfurl=" + "http://media.mtvnservices.com/player/release/?v=4.4.3" + " swfvfy=true"
    		item = xbmcgui.ListItem(path=finalurl)
        	xbmcplugin.setResolvedUrl(pluginhandle, True, item)
	elif link.find('mp4')<0: 
		clean = re.compile('rtmpe://cp10740.edgefcs.net/ondemand/mtvcomstor/_!/mtv.com/onair(.+?).flv').findall(link)[0]
		finalurl = "rtmpe://cp10740.edgefcs.net/ondemand/" + " playpath=mtvcomstor/_!/mtv.com/onair"+ clean + " swfurl=" + "http://media.mtvnservices.com/player/release/?v=4.4.3" + " swfvfy=true"
		item = xbmcgui.ListItem(path=finalurl)
        	xbmcplugin.setResolvedUrl(pluginhandle, True, item)
	elif link.find('onair')>0:
		clean = re.compile('rtmpe://cp10740.edgefcs.net/ondemand/mtvcomstor/_!/mtv.com/onair(.+?).mp4').findall(link)[-1]
		finalurl = "rtmpe://cp10740.edgefcs.net/ondemand/" + " playpath=mp4:mtvcomstor/_!/mtv.com/onair"+ clean + " swfurl=" + "http://media.mtvnservices.com/player/release/?v=4.4.3" + " swfvfy=true"
    		item = xbmcgui.ListItem(path=finalurl)
        	xbmcplugin.setResolvedUrl(pluginhandle, True, item)


def PLAYEPISODE(name,url):
	i=0
	req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
	match = re.compile('duration=".+?" url="(.+?)"').findall(link)
	for url in match:
		i=i+1
		if (settings['proxy'] == 'true'):
        		link= proxy(url,True)
        	else:
                	link= proxy(url)
		try:
			testip = re.compile('rtmpe:(.+?)\n').findall(link)[0]
		except:
			dialog = xbmcgui.Dialog()
			ok = dialog.ok("MTV Shows",'Your proxy IP is no longer working', 'or you need to enable the proxy.')
			return
		if 'mtvnorigin' in link:
			clean2 = re.compile('rtmpe://cp10740.edgefcs.net/ondemand/mtvnorigin/gsp.originmusicstor/sites/mtv.com/(.+?).mp4').findall(link)[-1]
			finalurl2 = "rtmpe://cp10740.edgefcs.net/ondemand/" + " playpath=mp4:mtvnorigin/gsp.originmusicstor/sites/mtv.com/"+ clean2 + " swfurl=" + "http://media.mtvnservices.com/player/release/?v=4.4.3" + " swfvfy=true"
			addLink('Part # '+str(i),finalurl2,'','','')
		elif link.find('mp4')>0:
			clean = re.compile('rtmpe://cp10740.edgefcs.net/ondemand/mtvcomstor/_!/mtv.com/onair(.+?).mp4').findall(link)[-1]
			finalurl = "rtmpe://cp10740.edgefcs.net/ondemand/" + " playpath=mp4:mtvcomstor/_!/mtv.com/onair"+ clean + " swfurl=" + "http://media.mtvnservices.com/player/release/?v=4.4.3" + " swfvfy=true"
			addLink('Part # '+str(i),finalurl,'','','')
		elif link.find('mp4')<0: 
			clean = re.compile('rtmpe://cp10740.edgefcs.net/ondemand/mtvcomstor/_!/mtv.com/onair(.+?).flv').findall(link)[0]
			finalurl = "rtmpe://cp10740.edgefcs.net/ondemand/" + " playpath=mtvcomstor/_!/mtv.com/onair"+ clean + " swfurl=" + "http://media.mtvnservices.com/player/release/?v=4.4.3" + " swfvfy=true"
			addLink('Part # '+str(i),finalurl,'','','')

def proxy( url, enableproxy = False ):
    try:
        if enableproxy == True:
        	us_proxy = 'http://' + xbmcplugin.getSetting(pluginhandle,'us_proxy') + ':' + xbmcplugin.getSetting(pluginhandle,'us_proxy_port')
            	print 'Using proxy: ' + us_proxy
            	proxy_handler = urllib2.ProxyHandler({'http':us_proxy})
            	opener = urllib2.build_opener(proxy_handler)
            	urllib2.install_opener(opener)
	
	req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
    except urllib2.URLError, e:
        print 'Error reason: ', e.reason
        return False
    else:
        return link    

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
        LISTING(url)
elif mode==2:
        print "PAGE"
        EP_CP(name,url)
elif mode==3:
        print "PAGE"
        EPISODES(url)
elif mode==4:
        print "PAGE"
        CLIPS(name,url)
elif mode==5:
        print "PAGE"
        PLAYCLIP(name,url)
elif mode==6:
        print "PAGE"
        PLAYEPISODE(name,url)
elif mode==7:
        print "PAGE"
        LISTING2(url)
elif mode==8:
        print "PAGE"
        LISTINGLATEST(url)
elif mode==9:
        print "PAGE"
        LISTINGPOPULAR(url)

xbmcplugin.endOfDirectory(int(sys.argv[1]))