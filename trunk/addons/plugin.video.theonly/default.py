import urllib,urllib2,re,sys,xbmcplugin,xbmcgui,cookielib,os,string,urlparse,xbmcaddon,base64

def CATS():
        addDir('Featured movies','http://www.theonlydevice.com/category/featured/page/1',2,'')
        addDir('Genres','pass',1,'')
        #addDir('Recently added','http://www.theonlydevice.com/',2,'')
	addDir('Search','http://www.theonlydevice.com/',5,'')

def INDEX(url,name):
        addDir('Asian','http://www.theonlydevice.com/genres/asian/',12,'')
        addDir('Animation','http://www.theonlydevice.com/genres/animation/page/1',12,'')
        addDir('Action','http://www.theonlydevice.com/genres/action/',12,'')
        addDir('Adventure','http://www.theonlydevice.com/genres/adventure/page/1',12,'')
        addDir('Biography','http://www.theonlydevice.com/genres/biography/page/1',12,'')
        addDir('Comedy','http://www.theonlydevice.com/genres/comedy/page/1',12,'')
        addDir('Crime','http://www.theonlydevice.com/genres/crime/',12,'')
        addDir('Documentary','http://www.theonlydevice.com/genres/documentary/',12,'')
        addDir('Drama','http://www.theonlydevice.com/genres/drama/',12,'')
        addDir('Family','http://www.theonlydevice.com/genres/family/',12,'')
        addDir('Fantasy','http://www.theonlydevice.com/genres/fantasy/',12,'')
        addDir('Film noir','http://www.theonlydevice.com/genres/film-noir/',12,'')
        addDir('Hindi','http://www.theonlydevice.com/genres/hindi/',12,'')
        addDir('History','http://www.theonlydevice.com/genres/history/',12,'')
        addDir('Horror','http://www.theonlydevice.com/genres/horror/',12,'')
        addDir('Music','http://www.theonlydevice.com/genres/music/',12,'')
        addDir('Musical','http://www.theonlydevice.com/genres/musical/',12,'')
        addDir('Mystery','http://www.theonlydevice.com/genres/mystery/',12,'')
        addDir('Romance','http://www.theonlydevice.com/genres/romance/',12,'')
        addDir('Sci-fi','http://www.theonlydevice.com/genres/sci-fi/',12,'')
        addDir('Sport','http://www.theonlydevice.com/genres/sport/',12,'')
        addDir('Thriller','http://www.theonlydevice.com/genres/thriller/',12,'')
        addDir('War','http://www.theonlydevice.com/genres/war/',12,'')
        addDir('Western','http://www.theonlydevice.com/genres/western/',12,'')

def INDEX2(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req).read()
	code=re.sub('&quot;','',response)
	code1=re.sub('&#039;','',code)
	code2=re.sub('&#215;','',code1)
	code3=re.sub('&#038;','',code2)
	code4=re.sub('&#8216;','',code3)
	code5=re.sub('&#8217;','',code4)
       	code6=re.sub('&amp;','&',code5)
        code7=re.sub("`",'',code6)
	urls=re.compile('</a><a href="(.+?)" title=".+?"><img style="background.+?"').findall(code7)
	names=re.compile('</a><a href=".+?" title="(.+?)"><img style="background.+?"').findall(code7)
	thumbs=re.compile('<img style="background: .+?/images/(.+?)\)" class="thumb"').findall(response)
	match=re.compile('<a href="(.+?)" >&laquo; Older Entries</a></div>').findall(response)
	match2=re.compile('<a href="http://www.theonlydevice.com/page(.+?)" title="(.+?)">.+?</a>').findall(response)
	videos=[(names[i],urls[i],thumbs[i])for i in range (0,len(urls))]
 	for name,url,thumb in videos:
               	addDir(name.replace('&#8221;',' ').replace('&#8243;',' ').replace('&#8220;',' '),url,3,'http://www.theonlydevice.com/images/'+thumb)
	for url in match:
		addDir('older entries',url,2,'')
	for url,name in match2:
		addDir(' Go to page '+name.replace('&raquo;',' '),'http://www.theonlydevice.com/page'+url,2,'http://www.clker.com/cliparts/0/5/7/9/1195435734741708243kuba_arrow_button_set_2.svg.hi.png')

def INDEX3(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req).read()
	code=re.sub('&quot;','',response)
	code1=re.sub('&#039;','',code)
	code2=re.sub('&#215;','',code1)
	code3=re.sub('&#038;','',code2)
	code4=re.sub('&#8216;','',code3)
	code5=re.sub('&#8217;','',code4)
       	code6=re.sub('&amp;','&',code5)
        code7=re.sub("`",'',code6)
	urls=re.compile('<a href="(.+?)" title=".+?"><img style="background.+?"').findall(code7)
	names=re.compile('<a href=".+?" title="(.+?)"><img style="background.+?"').findall(code7)
	thumbs=re.compile('<img style="background: .+?/images/(.+?)\)" class="thumb"').findall(response)
	match=re.compile('<a href="(.+?)" >&laquo; Older Entries</a></div>').findall(response)
	match2=re.compile('<a href="http://www.theonlydevice.com/page(.+?)" title="(.+?)">.+?</a>').findall(response)
	videos=[(names[i],urls[i],thumbs[i])for i in range (0,len(urls))]
 	for name,url,thumb in videos:
               	addDir(name.replace('&#8221;',' ').replace('&#8243;',' ').replace('&#8220;',' '),url,3,'http://www.theonlydevice.com/images/'+thumb)
	for url in match:
		addDir('older entries',url,12,'')
	for url,name in match2:
		addDir(' Go to page '+name.replace('&raquo;',' '),'http://www.theonlydevice.com/page'+url,12,'http://www.clker.com/cliparts/0/5/7/9/1195435734741708243kuba_arrow_button_set_2.svg.hi.png')

def PARTS(url,name):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        ref=response.geturl()
        link=response.read()
      	mvs=re.compile('<p><a href="http://www.movshare.net/(.+?)"').findall(link)
      	mvs2=re.compile('<p><a href="http://www2.movshare.net/(.+?)"').findall(link)
      	wisevid=re.compile('<p><a href="http://www.wisevid.com/(.+?)"').findall(link)
      	n=re.compile('<p><a href="http://www.novamov.com/video/(.+?)"').findall(link)
      	stg=re.compile('<p><a href="http://stagevu.com/video/(.+?)"').findall(link)
      	fst=re.compile('<p><a href="http://www.freestreamtube.com/v/(.+?)"').findall(link)
      	dvst=re.compile('<p><a href="http://divxstage.net/player.php?(.+?)"').findall(link)
      	dvst2=re.compile('<p><a href="http://divxstage.net/play.php?(.+?)"').findall(link)
      	dvden=re.compile('<p><a href="http://www.vidxden.com/(.+?)"').findall(link)
     	dvst3=re.compile('href="http://www.divxstage.net/video/(.+?)"').findall(link)
	img=re.compile('<img src="http://www.theonlydevice.com/images/(.+?)"').findall(link)
	info=re.compile('<meta name="description" content="(.+?)" />').findall(link)
	xt=re.compile('<p><a href="http://xtshare.com/(.+?)"').findall(link)
	vidr=re.compile('<p><a href="http://vidreel.com/(.+?)"').findall(link) 
	for url in mvs:
		addDir(name+' (movshare)','http://www.movshare.net/'+url,7,'http://www.theonlydevice.com/images/'+img[0],info[0])
	for url in mvs2:
		addDir(name+' (movshare)','http://www2.movshare.net/'+url,7,'http://www.theonlydevice.com/images/'+img[0],info[0])
	for url in dvden:
		addDir(name+' (vidxden)','http://www.vidxden.com/'+url,6,'http://www.theonlydevice.com/images/'+img[0],info[0])
	for url in xt:
		addDir(name+' (xtshare)','http://xtshare.com/'+url,8,'http://www.theonlydevice.com/images/'+img[0],info[0])
	for url in vidr:
		addDir(name+' (vidreel)','http://vidreel.com/'+url,9,'http://www.theonlydevice.com/images/'+img[0],info[0])
	for url in wisevid:
		addDir(name+' (wisevid)','http://www.wisevid.com/'+url,10,'http://www.theonlydevice.com/images/'+img[0],info[0])
	for url in dvst3:
		addDir(name+' (divxstage)','http://www.divxstage.net/video/'+url,11,'http://www.theonlydevice.com/images/'+img[0],info[0])
	for url in dvst2:
		addDir(name+' (divxstage)','http://divxstage.net/player.php?'+url,11,'http://www.theonlydevice.com/images/'+img[0],info[0])
	for url in dvst3:
		addDir(name+' (divxstage)','http://divxstage.net/player.php?'+url,11,'http://www.theonlydevice.com/images/'+img[0],info[0])

def divxden(url,name):
      	req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
   	response = urllib2.urlopen(req)
	link2=response.read()
	fcodenm=re.compile('name="fname" type="hidden" value="(.+?)"').findall(link2)[0]
	fcodeid=re.compile('name="id" type="hidden" value="(.+?)"').findall(link2)[0]
	print fcodenm
	try:
		values = {'op': 'download1','usr_login': ' ','id': fcodeid, 'fname': fcodenm,'referer' : ' ', 'method_free':'Continue to Video'}
		user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		headers = { 'User-Agent' : user_agent }
		data = urllib.urlencode(values)
		req = urllib2.Request(url, data, headers)
		response = urllib2.urlopen(req)
		link = response.read()

		file=re.compile("pluginspage(.+?)video").findall(link)[0]
		cleanup=file.replace('|',' ').replace('||',' ')
		hashlong = cleanup[-46:].replace(' ','')
		rawhashshort = re.compile('divxden(.+?)np_vid').findall(link)[0]
		hashshort =  re.compile('divxden(.+?)src').findall(link)[0]
   		finalurl = 'http://'+hashshort.replace('the','').replace('you','').replace(' ','').replace('|','')+'.divxden.com:182/d/'+hashlong+'/'+ fcodenm
		item = xbmcgui.ListItem(name)
        	ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(finalurl, item)
		addLink('Play',finalurl,'http://www.bitdefender.com/files/KnowledgeBase/img/movie_icon.png')
	except: pass

def movshare(url,name):
		user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		values = {'name' : 'watch','action' : '#'}
		headers = { 'User-Agent' : user_agent }
		data = urllib.urlencode(values)
		req = urllib2.Request(url, data, headers)
		response = urllib2.urlopen(req)
		the_page = response.read()
		swap=re.compile('<embed type="video/divx" src="(.+?)&.+?"').findall(the_page)
		if not swap: swap=re.compile('<embed type="video/divx" src="(.+?)"').findall(the_page)
		if not swap: swap=re.compile('"file","(.+?)&ec_rate=.+?"').findall(the_page)
		for url in swap:
			addLink('Play'+name,swap[0],'http://www.bitdefender.com/files/KnowledgeBase/img/movie_icon.png')

def xt(url,name):
      	req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
      	link=response.read()
        cookie=response.info()['Set-Cookie']
	code=re.compile('action=".+?Id=(.+?)"').findall(link)[0]
        url2=response.geturl()
	url3='http://xtshare.com/toshare.php?Id='+code

	user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.86 Safari/533.4'
	values = {'submit' : 'I am human now let me watch this video'}
	headers = { 'User-Agent' : user_agent, 'Referer' : 'http://xtshare.com/humancheck.php?Id='+code, 'Cookie': cookie}
	data = urllib.urlencode(values)
	req = urllib2.Request(url3, data, headers)
        response = urllib2.urlopen(req)
        link2=response.read()
	pagurl=response.geturl()
	rt1=re.compile("'rtmp://(.+?)'").findall(link2)[0]
	rt2=re.compile("file','(.+?)'").findall(link2)[0]

	item = xbmcgui.ListItem(name.replace('(xtshare)',''))
	finalurl = "rtmp://"+rt1 + "mp4:"+ rt2
	swfUrl = "http://xtshare.com/player.swf"
	tcUrl = "rtmp://"+rt1
        playPath = "mp4:"+rt2
	pageurl = pagurl
        item.setProperty("SWFPlayer", swfUrl)
        item.setProperty("PlayPath", playPath)
	item.setProperty("tcUrl", tcUrl)
	item.setProperty("PageURL", pageurl)
	item.setProperty("app", "vod/")
        ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(finalurl, item)
	addLink(name,'','')

def vidr(url,name):
      	req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
      	link=response.read()
        cookie=response.info()['Set-Cookie']
      	ref=response.geturl()
	match=re.compile('<p><a href=../../video/(.+?)/').findall(link)[0]
	url2='http://vidreel.com/video/'+match+'/'
  	user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.86 Safari/533.4'
	values = {'name' : 'watch','action' : '#'}
	headers = { 'User-Agent' : user_agent, 'Referer' : ref, 'Cookie': cookie}
	data = urllib.urlencode(values)
	req = urllib2.Request(url2, data, headers)
        response = urllib2.urlopen(req)
      	link2=response.read()
	pagurl=response.geturl()

	rt1=re.compile("'rtmp://(.+?)'").findall(link2)[0]
	rt2=re.compile("file','(.+?)'").findall(link2)[0]

	item = xbmcgui.ListItem(name.replace('(vidreel)',''))
	finalurl = "rtmp://"+rt1 + "mp4:"+ rt2
	swfUrl = "http://vidreel.com/player.swf"
	tcUrl = "rtmp://"+rt1
        playPath = "mp4:"+rt2
	pageurl = pagurl
        item.setProperty("SWFPlayer", swfUrl)
        item.setProperty("PlayPath", playPath)
	item.setProperty("tcUrl", tcUrl)
	item.setProperty("PageURL", pageurl)
	item.setProperty("app", "vod/")
        ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(finalurl, item)
	addLink(name,'','')

def wisevid(url,name):
      	req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
	link2=response.read()
	try:
		rawcode=re.compile("javascript:location.href='(.+?)'").findall(link2)[1]
		ref=response.geturl()
		values = {'name': 'no','value': 'Yes, let me watch'}
		user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.307.11 Safari/532.9'
		headers = { 'User-Agent' : user_agent, 'Referer': ref}
		data = urllib.urlencode(values)
		req = urllib2.Request(rawcode, data, headers)
		response = urllib2.urlopen(req)
		link3 = response.read()
		acode=re.compile('<input type="hidden" name="a" value="(.+?)" />').findall(link3)[0]
		vcode=re.compile('<input type="hidden" name="v" value="(.+?)" />').findall(link3)[0]
		url2='http://www.wisevid.com/play?v='+vcode
		values = {'a': acode,'v': vcode, 'no1' : 'Yes, let me watch'}
		user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.307.11 Safari/532.9'
		headers = { 'User-Agent' : user_agent, 'Referer': 'http://www.wisevid.com/gate-way?v='+vcode}
		data = urllib.urlencode(values)
		req = urllib2.Request(url2, data, headers)
		response = urllib2.urlopen(req)
		link = response.read()
		match=re.compile("getF(\(.+?)'").findall(link)[0]
		clean= match.replace("('","")
		finalurl=base64.decodestring(clean)
		item = xbmcgui.ListItem(name)
        	ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(finalurl, item)
		addLink('Play',finalurl,'http://www.bitdefender.com/files/KnowledgeBase/img/movie_icon.png')
	except: pass
	try:
		acode=re.compile('<input type="hidden" name="a" value="(.+?)" />').findall(link2)[0]
		vcode=re.compile('<input type="hidden" name="v" value="(.+?)" />').findall(link2)[0]
		url2='http://www.wisevid.com/play?v='+vcode
		values = {'a': acode,'v': vcode, 'no1' : 'Yes, let me watch'}
		user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.307.11 Safari/532.9'
		headers = { 'User-Agent' : user_agent, 'Referer': 'http://www.wisevid.com/gate-way?v='+vcode}
		data = urllib.urlencode(values)
		req = urllib2.Request(url2, data, headers)
		response = urllib2.urlopen(req)
		link = response.read()
		match=re.compile("getF(\(.+?)'").findall(link)[0]
		clean= match.replace("('","")
		finalurl=base64.decodestring(clean)
		item = xbmcgui.ListItem(name)
        	ok=xbmc.Player(xbmc.PLAYER_CORE_DVDPLAYER).play(finalurl, item)
		addLink('Play',finalurl,'http://www.bitdefender.com/files/KnowledgeBase/img/movie_icon.png')
	except: pass

def dvst(url,name):
     	req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
	link=response.read()
	match=re.compile('<embed type="video/divx" src="(.+?)"').findall(link)[0]
	addLink('Play ',match,'http://www.bitdefender.com/files/KnowledgeBase/img/movie_icon.png')

def SEARCH():
        keyb = xbmc.Keyboard('', 'Search TheOnlyDevice')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
                req = urllib2.Request('http://www.theonlydevice.com/?s='+encode+'&x=0&y=0')
	        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                response = urllib2.urlopen(req).read()
		code=re.sub('&quot;','',response)
		code1=re.sub('&#039;','',code)
		code2=re.sub('&#215;','',code1)
	       	code3=re.sub('&#038;','',code2)
		code4=re.sub('&#8216;','',code3)
		code5=re.sub('&#8217;','',code4)
       		code6=re.sub('&amp;','&',code5)
        	code7=re.sub("`",'',code6)
		urls=re.compile('</a><a href="(.+?)" title=".+?"><img style="background.+?"').findall(code7)
		names=re.compile('</a><a href=".+?" title="(.+?)"><img style="background.+?"').findall(code7)
		thumbs=re.compile('<img style="background: .+?/images/(.+?)\)" class="thumb"').findall(response)
		match=re.compile('<a href="http://www.theonlydevice.com/page/(.+?)" title="(.+?)">.+?</a>').findall(response)
		videos=[(names[i],urls[i],thumbs[i])for i in range (0,len(urls))]
 		for name,url,thumb in videos:
               		addDir(name.replace('&#8221;',' ').replace('&#8243;',' ').replace('&#8220;',' '),url,3,'http://www.theonlydevice.com/images/'+thumb)
		for url,name in match:
			addDir('  Go to page '+name.replace('&raquo;',' '),'http://www.theonlydevice.com/page/'+url,2,'http://www.clker.com/cliparts/0/5/7/9/1195435734741708243kuba_arrow_button_set_2.svg.hi.png')

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
      
def addLink(name,url,thumbnail):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=thumbnail)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz)
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
        INDEX(url,name)
elif mode==2:
        print "PAGE"
        INDEX2(url,name)
elif mode==3:
        print "PAGE"
        PARTS(url,name)
elif mode==4:
        print "PAGE"
        VIDS(url,name)
elif mode==5:
        print "SEARCH  :"+url
        SEARCH()
elif mode==6:
        print "PAGE"
        divxden(url,name)
elif mode==7:
        print "PAGE"
        movshare(url,name)
elif mode==8:
        print "PAGE"
        xt(url,name)
elif mode==9:
        print "PAGE"
        vidr(url,name)
elif mode==10:
        print "PAGE"
        wisevid(url,name)
elif mode==11:
        print "PAGE"
        dvst(url,name)
elif mode==12:
        print "PAGE"
        INDEX3(url,name)
        
xbmcplugin.endOfDirectory(int(sys.argv[1]))