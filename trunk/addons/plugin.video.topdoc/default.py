import urllib,urllib2,re,sys,xbmcplugin,xbmcgui,cookielib,xbmcaddon
pluginhandle = int(sys.argv[1])


def CATS():
			addDir('Recently added','http://topdocumentaryfilms.com/all/',3,'')
			addDir('Featured documentaries','http://topdocumentaryfilms.com/',4,'')
			addDir('Most commented documentaries','http://topdocumentaryfilms.com/most-commented-documentaries/',10,'')
			addDir('Genres','http://topdocumentaryfilms.com/',13,'')
			addDir('Search','http://topdocumentaryfilms.com/',9,'')
			addDir('List All','http://topdocumentaryfilms.com/watch-online/',8,'')

def GENRE(url):
  			req = urllib2.Request(url)
        		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        		response = urllib2.urlopen(req)
			link=response.read()
			match=re.compile('href="http://topdocumentaryfilms.com/category/(.+?)" title="View all posts filed under .+?">(.+?)</a>').findall(link)
			for url,name in match:
				addDir(name,'http://topdocumentaryfilms.com/category/'+url,1,'','')

def LIST(url):
        		req=urllib2.Request(url)
                        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
                        response = urllib2.urlopen(req).read()
			code=re.sub('&quot;','',response)
			code1=re.sub('&#039;','',code)
			code2=re.sub('&#215;','',code1)
	       		code3=re.sub('&#038;','',code2)
			code4=re.sub('&#8216;','',code3)
			code5=re.sub('&#8217;','',code4)
			code6=re.sub('&#8211;','',code5)
			code7=re.sub('&#8220;','',code6)
			code8=re.sub('&#8221;','',code7)
			code9=re.sub('&#8212;','',code8)
    			code10=re.sub('&amp;','&',code9)
        		code11=re.sub("`",'',code10)
                       	lexus=re.compile('href="http://topdocumentaryfilms.com/(.+?)" rel="bookmark" title="(.+?)"').findall(code11)
			for url,name in lexus:
				addDir(name,'http://topdocumentaryfilms.com/'+url,2,'','')
	     
def INDEX(url):
        		req=urllib2.Request(url)
                        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
                        response = urllib2.urlopen(req).read()
			code=re.sub('&quot;','',response)
			code1=re.sub('&#039;','',code)
			code2=re.sub('&#215;','',code1)
	       		code3=re.sub('&#038;','',code2)
			code4=re.sub('&#8216;','',code3)
			code5=re.sub('&#8217;','',code4)
			code6=re.sub('&#8211;','',code5)
			code7=re.sub('&#8220;','',code6)
			code8=re.sub('&#8221;','',code7)
			code9=re.sub('&#8212;','',code8)
    			code10=re.sub('&amp;','&',code9)
        		code11=re.sub("`",'',code10)
                       	lexus=re.compile('href="(.+?)" title="(.+?)"><img\nsrc="(.+?)" alt=".+?" align="left" /></a>(.+?)</p><p\n').findall(code11)
                       	nxt=re.compile('href="(.+?)">Next</a></div></div><div').findall(code11)
			for url,name,thumb,plot in lexus:
				addDir(name,url,2,thumb,plot)
			for url in nxt:
				addDir('Next',url,1,'http://www.nws.noaa.gov/os/marine/safeboating/monday_files/next.gif','')

def INDEX2(url):
                        req=urllib2.Request(url)
                        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
                        response = urllib2.urlopen(req).read()
			code=re.sub('&quot;','',response)
			code1=re.sub('&#039;','',code)
			code2=re.sub('&#215;','',code1)
	       		code3=re.sub('&#038;','',code2)
			code4=re.sub('&#8216;','',code3)
			code5=re.sub('&#8217;','',code4)
			code6=re.sub('&#8211;','',code5)
			code7=re.sub('&#8220;','',code6)
			code8=re.sub('&#8221;','',code7)
			code9=re.sub('&#8212;','',code8)
    			code10=re.sub('&amp;','&',code9)
        		code11=re.sub("`",'',code10)
                       	lexus=re.compile('href="(.+?)" title="(.+?)"><img').findall(code11)
                        for url,name in lexus:
				addDir(name,url,2,'','')

def INDEX3(url):
                        req=urllib2.Request(url)
                        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
                        response = urllib2.urlopen(req).read()
			code=re.sub('&quot;','',response)
			code1=re.sub('&#039;','',code)
			code2=re.sub('&#215;','',code1)
	       		code3=re.sub('&#038;','',code2)
			code4=re.sub('&#8216;','',code3)
			code5=re.sub('&#8217;','',code4)
			code6=re.sub('&#8211;','',code5)
			code7=re.sub('&#8220;','',code6)
			code8=re.sub('&#8221;','',code7)
			code9=re.sub('&#8212;','',code8)
    			code10=re.sub('&amp;','&',code9)
        		code11=re.sub("`",'',code10)
                       	lexus=re.compile('href="(.+?)" title="(.+?)"><img').findall(code11)
                        for url,name in lexus:
				addDir(name,url,2,'','')

def INDEX4(url):
                        req=urllib2.Request(url)
                        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
                        response = urllib2.urlopen(req).read()
			code=re.sub('&quot;','',response)
			code1=re.sub('&#039;','',code)
			code2=re.sub('&#215;','',code1)
	       		code3=re.sub('&#038;','',code2)
			code4=re.sub('&#8216;','',code3)
			code5=re.sub('&#8217;','',code4)
			code6=re.sub('&#8211;','',code5)
			code7=re.sub('&#8220;','',code6)
			code8=re.sub('&#8221;','',code7)
			code9=re.sub('&#8212;','',code8)
    			code10=re.sub('&amp;','&',code9)
        		code11=re.sub("`",'',code10)
                       	lexus=re.compile('href="(.+?)" title="(.+?)"><img').findall(code11)
                        for url,name in lexus:
				addDir(name,url,2,'','')


def VIDS(url,name):
	i=0
	req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
	link=response.read()
	altcode=re.compile('href="http://www.youtube.com/view_play_list(.+?)"').findall(link)
	coderaw=re.compile('value="http://www.youtube.com/p/(.+?)"').findall(link)
	stagevu=re.compile('href="http://stagevu.com/(.+?)">StageVu</a>').findall(link)
        smalltitle=re.compile('target="_blank" href="(.+?)">(.+?)</a></strong>').findall(link)
	for code in stagevu:
		try:
			req = urllib2.Request('http://stagevu.com/'+code)
        		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        		response = urllib2.urlopen(req)
        		link=response.read()
      			vid=re.compile('<param name="src" value="(.+?)"').findall(link)[0]
			i=i+1
			addLink('Play from Stagevu'+' -'+' Part '+ str(i),vid,'','','')
		except:pass
	for url,name in smalltitle:
	        	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(2)
                	item=xbmcgui.ListItem('Play '+name)
          		item.setInfo( type="Video", infoLabels={ "Title": name} )                
			item.setProperty('IsPlayable', 'true')
                	xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)

	veehd=re.compile('href="http://veehd.com/video/(.+?)">VeeHD</a>').findall(link)
	for code in veehd:
		try:
			vhd = xbmcaddon.Addon(id='plugin.video.topdoc')
			uname = vhd.getSetting('uname')
			pwd   = vhd.getSetting('pwd')
			if (not uname or uname == '') or (not pwd or pwd == ''):
				d = xbmcgui.Dialog()
				d.ok('Welcome to VeeHD.com', 'Please enter your username and password','registered at the website')
				vhd.openSettings(sys.argv[ 0 ])

			urlogin = 'http://veehd.com/login'
			cookiejar = cookielib.LWPCookieJar()
			cookiejar = urllib2.HTTPCookieProcessor(cookiejar) 
			opener = urllib2.build_opener(cookiejar)
			urllib2.install_opener(opener)
 			values = {'ref': 'http://veehd.com/','uname': uname, 'pword': pwd, 'submit':'Login', 'terms':'on'}
			user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
			headers = { 'User-Agent' : user_agent }
			data = urllib.urlencode(values)
			req = urllib2.Request(urlogin, data, headers)
			response = urllib2.urlopen(req)

			req = urllib2.Request('http://veehd.com/video/'+code)
        		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        		response = urllib2.urlopen(req)
        		link=response.read()
      			match=re.compile('href="(.+?)"><b><u>Download video</u>').findall(link)[0]
			addLink('Play from VeeHD',match,'http://www.bitdefender.com/files/KnowledgeBase/img/movie_icon.png','','')
		except: pass

	for code in altcode:
		req = urllib2.Request("http://gdata.youtube.com/feeds/api/playlists/"+code.replace('?p=','')+"?&v=2&max-results=50")
        	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        	response = urllib2.urlopen(req)
		link=response.read()
		urlsingle = re.compile("part</media:keywords><media:player url='(.+?)'/><media:thumbnail").findall(link)
		urlsingle2 = re.compile("</title><link rel='alternate' type='text/html' href='(.+?)'").findall(link)
		for url in urlsingle:
			i=i+1
	        	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(14)
                	item=xbmcgui.ListItem('Play '+name.replace(' ','')+' -'+' Part '+ str(i))
          		item.setInfo( type="Video", infoLabels={ "Title": name} )                
			item.setProperty('IsPlayable', 'true')
                	xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)
		for url in urlsingle2:
			i=i+1
			u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(14)
                	item=xbmcgui.ListItem('Play '+name.replace(' ','')+' -'+' Part '+ str(i))
          		item.setInfo( type="Video", infoLabels={ "Title": name} )                
			item.setProperty('IsPlayable', 'true')
                	xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)

	for code in coderaw:
			codeplist = code[:16]
			match="http://gdata.youtube.com/feeds/api/playlists/"+codeplist+"?&v=2&max-results=50"
			print match
			req = urllib2.Request(match)
        		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        		response = urllib2.urlopen(req)
			link=response.read()
			urlsingle = re.compile("part</media:keywords><media:player url='(.+?)'/><media:thumbnail").findall(link)
			urlsingle2 = re.compile("</title><link rel='alternate' type='text/html' href='(.+?)'").findall(link)
			for url in urlsingle:
				i=i+1
	        		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(14)
                		item=xbmcgui.ListItem('Play '+name.replace(' ','')+' -'+' Part '+ str(i))
          			item.setInfo( type="Video", infoLabels={ "Title": name} )                
				item.setProperty('IsPlayable', 'true')
                		xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)
			for url in urlsingle2:
				i=i+1
	        		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(14)
                		item=xbmcgui.ListItem('Play '+name.replace(' ','')+' -'+' Part '+ str(i))
          			item.setInfo( type="Video", infoLabels={ "Title": name} )                
				item.setProperty('IsPlayable', 'true')
                		xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)


	try:
		coderaw2=re.compile('value="http://www.youtube.com/v/(.+?)"').findall(link)[0]
		codeplist2 = coderaw2[:11]
		req = urllib2.Request('http://www.youtube.com/watch?v='+codeplist2)
		response = urllib2.urlopen(req)
		link = response.read()
		finalurl=re.compile('fmt_url_map=.+?%7Chttp%3A%2F%2F(.+?)%2C.+?%7Chttp').findall(link)[0]
		addLink('Play '+name,'http://'+finalurl.replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%25','%').replace('%2F','/').replace('%26','&'),'','','')
	except: pass

	try:
		coderaw2=re.compile('"http://www.youtube.com/embed/(.+?)"').findall(link)[0]
		codeplist2 = coderaw2.replace('?rel=0','')
		req = urllib2.Request('http://www.youtube.com/watch?v='+codeplist2)
		response = urllib2.urlopen(req)
		link = response.read()
		finalurl=re.compile('fmt_url_map=.+?%7Chttp%3A%2F%2F(.+?)%2C.+?%7Chttp').findall(link)[0]
		addLink('Play '+name,'http://'+finalurl.replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%25','%').replace('%2F','/').replace('%26','&'),'','','')
	except: pass


	try:
      		gubacode=re.compile("src='http://www.guba.com/.+?bid=(.+?)' quality='.+?'").findall(link)[0]
		flvpath="http://www.guba.com/playerConfig?isEmbeddedPlayer=true&bid="+gubacode
		req = urllib2.Request(flvpath)
        	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        	response = urllib2.urlopen(req);
		link=response.read()
		match = re.compile('"url":"(.+?)?mt').findall(link)
    		for url in match:
                	addLink('Play (guba) '+name,url,'','','')
	except: pass

	try:
		blp=re.compile('src="http://blip.tv/play/(.+?)"').findall(link)
		for code in blp:
			req = urllib2.Request('http://www.flashvideodownloader.org/download2.php?u=http://blip.tv/play/'+code)
        		req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        		page = urllib2.urlopen(req);new=page.read();page.close()
        		dw=re.compile('<p>Click Here to download </a></p><a href="(.+?)"').findall(new)
        		for url in dw:
				addLink('Play '+name,url,'','','')
	except: pass

	try:
		blp=re.compile('value="file=(.+?)flv').findall(link)[0]
		addLink('Play '+name,'http://server1.sureynot.com/xmoov.php?file='+blp+'flv','','','')
	except: pass

	try:
		vid=re.compile('"http://videos.engagemedia.org/(.+?)"').findall(link)[0]
		addLink('Play '+name+ ' (Full)','http://videos.engagemedia.org/'+vid,'','','')
	except: pass

	try:
		swap=re.compile('clip_id=(.+?)&amp;server=vimeo').findall(link)
		if not swap: swap=re.compile('"http://player.vimeo.com/video/(.+?)?title').findall(link)
		for code in swap:
			try:
				url='http://www.flashvideodownloader.org/download2.php?u=http://vimeo.com/'+code.replace('?','')
				req = urllib2.Request(url)
        			req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        			req.add_header('Referer', 'http://www.flashvideodownloader.org/')
        			page = urllib2.urlopen(req);new=page.read();page.close()
				dw=re.compile('http://av.vimeo.com/(.+?)\n').findall(new)[0]
				addLink('Play '+name+ ' (Full)','http://av.vimeo.com/'+dw,'','','')
			except: pass
	except: pass

	try:
		vid=re.compile('value="http://www.dailymotion.com/swf/video/(.+?)?additionalInfos=0"').findall(link)
		vid2=re.compile('src="http://www.dailymotion.com/(.+?)"').findall(link)
		for url in vid:
			req = urllib2.Request(url)
			response = urllib2.urlopen(req)
			link = response.read()
			finalurl=re.compile('"video", "http://www.dailymotion.com/cdn/(.+?)"').findall(link)
			for url in finalurl:
				addLink('Play '+name,'http://www.dailymotion.com/cdn/'+url,'','','')
		for url in vid2:
			req = urllib2.Request('http://www.dailymotion.com/'+url)
			response = urllib2.urlopen(req)
			link = response.read()
			url2 = re.compile('"/widget/(.+?)"').findall(link)[0]
			req = urllib2.Request('http://www.dailymotion.com/widget/'+url2)
			response = urllib2.urlopen(req)
			link = response.read()
			url3 = re.compile('id="jukebox_nav_tabs"><li name="(.+?)"').findall(link)[0]
			req = urllib2.Request('http://www.dailymotion.com/json/internal'+url3)
			response = urllib2.urlopen(req)
			link = response.read()
			finalurl = re.compile('"stream_flv_mini_url":"(.+?)"').findall(link)
			for url in finalurl:
				i=i+1
				addLink('Play '+name+' -'+' Part '+ str(i),url.replace('€','').replace('/',''),'','','')
	except: pass

	try:
		swap=re.compile('src=".+?docId=(.+?)"').findall(link)
		if not swap: swap=re.compile('<embed style=".+?" id=".+?" type="application/x-shockwave-flash" src=".+?docId=(.+?)" allowFullScreen="true"').findall(link)
		if not swap: swap=re.compile('src=".+?docid=(.+?)&#038;hl=un"').findall(link)
		if not swap: swap=re.compile('src=".+?docid=(.+?)&#038;hl=en"').findall(link)
		if not swap: swap=re.compile('src=.+?docid=(.+?)&#038;hl=en&#038;fs=true').findall(link)
		if not swap: swap=re.compile("docid:'(.+?)'").findall(link)
		for code in swap:
			try:
				req = urllib2.Request('http://video.google.com/videofeed?fgvns=1&fai=1&docid='+code+'&hl=undefined')
				response = urllib2.urlopen(req)
				link2 = response.read()
        			dw=re.compile('content url="(.+?)" type="video/x-flv"').findall(link2)[0]
				finalurl=dw.replace('amp;','')
 				item = xbmcgui.ListItem(path=finalurl)
        			xbmcplugin.setResolvedUrl(pluginhandle, True, item)
			except: pass
	except: pass

        try:
		code=re.compile('flashvars.v = "(.+?)"').findall(link)[0]
		code=re.compile('"http://www.megavideo.com/v/(.+?)"').findall(link)[0]
                req = urllib2.Request("http://www.megavideo.com/xml/videolink.php?v="+code)
                req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
                req.add_header('Referer', 'http://www.megavideo.com/')
                lemon = urllib2.urlopen(req);response=lemon.read();lemon.close()
                errort = re.compile(' errortext="(.+?)"').findall(response)
                if len(errort) > 0: addLink(errort[0],'http://novid.com','')
                else:
                        s = re.compile(' s="(.+?)"').findall(response)
                        k1 = re.compile(' k1="(.+?)"').findall(response)
                        k2 = re.compile(' k2="(.+?)"').findall(response)
                        un = re.compile(' un="(.+?)"').findall(response)
                        movielink = "http://www" + s[0] + ".megavideo.com/files/" + __calculateFileHash(un[0], k1[0], k2[0]) + "/?.flv"
			item = xbmcgui.ListItem(path=movielink)
        		xbmcplugin.setResolvedUrl(pluginhandle, True, item)
        except: pass
	
	code=re.compile('value="http://www.megavideo.com/v/(.+?)"').findall(link)
	for url in code:
		try:
	        	u=sys.argv[0]+"?url="+urllib.quote_plus('http://www.megavideo.com/v/'+url)+"&mode="+str(2)
        		item=xbmcgui.ListItem('Play '+name)
          		item.setInfo( type="Video", infoLabels={ "Title": name} )                
			item.setProperty('IsPlayable', 'true')
                	xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)
		except: pass
		
def Youtube(url,name):
	req = urllib2.Request(url)
	response = urllib2.urlopen(req)
	link = response.read()
	code=re.compile('fmt_url_map=.+?%7Chttp%3A%2F%2F(.+?)%2C.+?%7Chttp').findall(link)[0]
	finalurl='http://'+code.replace('%2F','/').replace('%3F','?').replace('%3D','=').replace('%25','%').replace('%2F','/').replace('%26','&')
 	item = xbmcgui.ListItem(path=finalurl)
        xbmcplugin.setResolvedUrl(pluginhandle, True, item)

def VEEHD(url):
	vhd = xbmcaddon.Addon(id='plugin.video.topdoc')

	uname = vhd.getSetting('uname')
	pwd   = vhd.getSetting('pwd')
	if (not uname or uname == '') or (not pwd or pwd == ''):
		d = xbmcgui.Dialog()
		d.ok('Welcome to veehd.com', 'Please enter your username and password','registered at VeeHD.com')
		vhd.openSettings(sys.argv[ 0 ])

	urlogin = 'http://veehd.com/login'
	cookiejar = cookielib.LWPCookieJar()
	cookiejar = urllib2.HTTPCookieProcessor(cookiejar) 
	opener = urllib2.build_opener(cookiejar)
	urllib2.install_opener(opener)
 	values = {'ref': 'http://veehd.com/','uname': uname, 'pword': pwd, 'submit':'Login', 'terms':'on'}
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	headers = { 'User-Agent' : user_agent }
	data = urllib.urlencode(values)
	req = urllib2.Request(urlogin, data, headers)
	response = urllib2.urlopen(req)

	req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
      	match=re.compile('href="(.+?)"><b><u>Download video</u>').findall(link)[0]
	addLink('Play',match,'http://www.bitdefender.com/files/KnowledgeBase/img/movie_icon.png','','')

def STGVU(url):
	req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
      	m=re.compile("'http://n64.stagevu.com/v/(.+?).avi';").findall(link)[0]
	addLink('Play','http://n42.stagevu.com/v/'+m+'.avi','','','')

def __calcDecriptionMix(hash, keyMix):
  """Mixes the decription keys into the hash and returns the updated hash
  @param hash: the hash to merge the keys into
  @param keyMix: the array of keys to mix"""
  for i in range(128):
    hash[i] = str(int(hash[i]) ^ int(keyMix[i + 256]) & 1)
  return "".join(hash)

def __toHexDecriptionString(binaryChunks):
  """Converts an array of binary strings into a string of the corresponding hex chunks merged
  This method will first loop through the binary strings converting each one into it's correspondent
  hexadecimal string and then merge the resulting array into a string
  @param binaryChunks: an array of binary strings
  @return: a string of the corresponding hexadecimal strings, merged"""
  hexChunks = []
  for binChunk in binaryChunks:
    hexChunks.append("%x" % int(binChunk, 2))    
  return "".join(hexChunks)

def __doDecriptionChunks(binaryMergedString):
  """Break a string of 0's and 1's in pieces of 4 chars
  @param binaryMergedString: a string of 0's and 1's to break in 4-part pieces
  @return: an array of 4 character parts of the original string"""
  binaryChunks = []
  for index in range(0, len(binaryMergedString), 4):
    binaryChunk = binaryMergedString[index:index + 4]
    binaryChunks.append(binaryChunk)
  return binaryChunks

def __doDecriptionSwaps(hash, keys):
  """Swap the first 256 indices from keys on the hash with the last 128 elements from the hash
  @param hash: the hash to do swaps on
  @param keys: the generated keys to use as indices for the swaps
  @return: hash after swaps"""
  for index in range(256, 0, -1):
    key = keys[index]
    swapTarget = index % 128
    oldHashKey = hash[key]
    hash[key] = hash[swapTarget]
    hash[swapTarget] = oldHashKey
  return hash

def __computeIndices(key1, key2):
  """Generate an array of 384 indices with values 0-127
  @param key1: first seed to generate indices from
  @param key2: second seed to generate indices from
  @return: an array of 384 indices with values between 0 and 127"""
  indices = []
  for i in range(384):
    key1 = (int(key1) * 11 + 77213) % 81371
    key2 = (int(key2) * 17 + 92717) % 192811
    indices.append((int(key1) + int(key2)) % 128)
  return indices

def __explodeBin(str1):
  # explode each char in str1 into it;s binary representation
  # and collect the result into __reg1
  __reg1 = []
  __reg3 = 0
  while (__reg3 < len(str1)):
    __reg0 = str1[__reg3]
    holder = __reg0
    if (holder == "0"):
      __reg1.append("0000")
    else:
      if (__reg0 == "1"):
        __reg1.append("0001")
      else:
        if (__reg0 == "2"): 
          __reg1.append("0010")
        else: 
          if (__reg0 == "3"):
            __reg1.append("0011")
          else: 
            if (__reg0 == "4"):
              __reg1.append("0100")
            else: 
              if (__reg0 == "5"):
                __reg1.append("0101")
              else: 
                if (__reg0 == "6"):
                  __reg1.append("0110")
                else: 
                  if (__reg0 == "7"):
                    __reg1.append("0111")
                  else: 
                    if (__reg0 == "8"):
                      __reg1.append("1000")
                    else: 
                      if (__reg0 == "9"):
                        __reg1.append("1001")
                      else: 
                        if (__reg0 == "a"):
                          __reg1.append("1010")
                        else: 
                          if (__reg0 == "b"):
                            __reg1.append("1011")
                          else: 
                            if (__reg0 == "c"):
                              __reg1.append("1100")
                            else: 
                              if (__reg0 == "d"):
                                __reg1.append("1101")
                              else: 
                                if (__reg0 == "e"):
                                  __reg1.append("1110")
                                else: 
                                  if (__reg0 == "f"):
                                    __reg1.append("1111")

    __reg3 = __reg3 + 1
  return list("".join(__reg1))

def __calculateFileHash(str1, key1, key2):
  # explode hex to bin strings, collapse to a string and return char array
  hash = __explodeBin(str1)
  # based on the keys, generate an array of 384 (256 + 128) values
  decriptIndices = __computeIndices(key1, key2)
  # from 256 to 0, swap hash[decriptIndices[x]] with hash[__reg3 % 128]
  hash = __doDecriptionSwaps(hash, decriptIndices)
  # replace the first 128 chars in hash with the formula:
  #  hash[x] = hash[x] * decriptIndices[x+256] & 1
  hash = __calcDecriptionMix(hash, decriptIndices)
  # split __reg12 in chunks of 4 chars
  chunks = __doDecriptionChunks(hash)  
  # convert each binary chunk to a hex string for the final hash
  return __toHexDecriptionString(chunks)

def SEARCH():
        keyb = xbmc.Keyboard('', 'Search TopDocumentaryFilms')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
		sURL = 'http://www.google.com/cse?cx=partner-pub-2600122794880266%3Auqpjg8s2z8l&cof=FORID%3A11&ie=UTF-8&q='+encode+'&sa=Search&ad=w9&num=150&rurl=http://topdocumentaryfilms.com/search/?cx=partner-pub-2600122794880266%3Auqpjg8s2z8l&cof=FORID%3A11&ie=UTF-8&q='+encode+'&sa=Search'
		user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
		req = urllib2.Request(sURL)
        	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
		response = urllib2.urlopen(req)
		link = response.read()
		match=re.compile('class=r><a href="(.+?)" target=_top class=l onmousedown=".+?">(.+?)Watch Free Documentary Online').findall(link)
		nxt=re.compile('<a href="(.+?)"><span>Next</span>').findall(link)
		for url,name in match:
			addDir(name.replace('<em>','').replace('</em>','').replace('|','').replace('&#039;',''),url,2,'','')

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
        INDEX(url)
elif mode==2:
        print "PAGE"
        VIDS(url,name)
elif mode==3:
        print "PAGE"
        INDEX2(url)
elif mode==4:
        print "PAGE"
        INDEX3(url)
elif mode==5:
        print "PAGE"
        STGVU(url)
elif mode==10:
        print "PAGE"
        INDEX4(url)
elif mode==7:
        print "PAGE"
        VEEHD(url)
elif mode==8:
        print "LIST"
        LIST(url)
elif mode==9:
        print "SEARCH  :"+url
        SEARCH()
elif mode==13:
        print "PAGE"
        GENRE(url)
elif mode==14:
        print "PAGE"
        Youtube(url,name)
        
xbmcplugin.endOfDirectory(int(sys.argv[1]))