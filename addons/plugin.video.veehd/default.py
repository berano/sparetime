import urllib,urllib2,re,sys,xbmcplugin,xbmcgui
import cookielib,os,string,cookielib,xbmcaddon

vhd = xbmcaddon.Addon(id='plugin.video.veehd')
pluginhandle = int(sys.argv[1])


def CATS():
        addDir('Channels','http',1,'')
        addDir('Recent','http://veehd.com/recent',2,'')
        addDir('Popular','http://veehd.com/popular',2,'')
        addDir('Search','http://veehd.com/',4,'')
        addDir('1080p','http://veehd.com/search?res=1080p',2,'')
        addDir('720p','http://veehd.com/search?res=720p',2,'')

def CHN(url):
        addDir('Animation','http://veehd.com/search?tag=animation',2,'')
        addDir('Art','http://veehd.com/search?tag=art',2,'')
        addDir('Blogs','http://veehd.com/search?tag=blogs',2,'')
        addDir('Comedy','http://veehd.com/search?tag=comedy',2,'')
        addDir('Educational','http://veehd.com/search?tag=educational',2,'')
        addDir('Games','http://veehd.com/search?tag=games',2,'')
        addDir('Music','http://veehd.com/search?tag=music',2,'')
        addDir('News','http://veehd.com/search?tag=news',2,'')
        addDir('Sport','http://veehd.com/search?tag=sport',2,'')
        addDir('Other','http://veehd.com/search?tag=other',2,'')
       
def INDEX(url,name):
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
        req.add_header('User-Agent', user_agent)
        response = urllib2.urlopen(req)
        link=response.read()
	thumbs=re.compile('<img id="img.+?" src="(.+?)"').findall(link)
      	names=re.compile('<a href="/video/.+?">(.+?)</a>').findall(link)
	urls=re.compile('<a href="/video/(.+?)">.+?</a>').findall(link)
	videos=[(thumbs[i],names[i],urls[i])for i in range (0,len(urls))]
	nxt=re.compile('</a></li><li class="nextpage"><a rel="nofollow" href="(.+?)">&raquo;</a></li>			</ul>').findall(link)
	for thumb,name,url in videos:
	        u=sys.argv[0]+"?url="+urllib.quote_plus('http://veehd.com/video/'+url,name)+"&mode="+str(3)
                item=xbmcgui.ListItem(name, iconImage=thumb)
          	item.setInfo( type="Video", infoLabels={ "Title": name} )                
		item.setProperty('IsPlayable', 'true')
                xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=item)
	for url in nxt:
		addDir('Next page','http://veehd.com'+url,2,'')

def VIDEO(url):
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
  	item = xbmcgui.ListItem(path=match)
        xbmcplugin.setResolvedUrl(pluginhandle, True, item)

def SEARCH():
        keyb = xbmc.Keyboard('', 'Search VEEHD')
        keyb.doModal()
        if (keyb.isConfirmed()):
                search = keyb.getText()
                encode=urllib.quote(search)
                req = urllib2.Request('http://veehd.com/search?q='+encode)
	        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
                link = urllib2.urlopen(req).read()
   		thumbs=re.compile('<img id="img.+?" src="(.+?)"').findall(link)
      		names=re.compile('<a href="/video/.+?">(.+?)</a>').findall(link)
		urls=re.compile('<a href="/video/(.+?)">.+?</a>').findall(link)
		videos=[(thumbs[i],names[i],urls[i])for i in range (0,len(urls))]
		nxt=re.compile('href="(.+?)&page=2">&raquo;</a></li>').findall(link)
		for thumb,name,url in videos:
			addDir(name,'http://veehd.com/video/'+url,3,thumb)
		for url in nxt:
			addDir('Next page','http://veehd.com'+url+'&page=2',2,'')

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

        

def addDir(name,url,mode,thumbnail):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=thumbnail)
        liz.setInfo( "video", { "Title":name})
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

def check_settings():
		uname = vhd.getSetting('uname')
		pwd   = vhd.getSetting('pwd')
		if (not uname or uname == '') or (not pwd or pwd == ''):
				d = xbmcgui.Dialog()
				d.ok('Welcome to veehd.com', 'To start using this plugin first go to veehd.com','and create an (free) account.')
				vhd.openSettings(sys.argv[ 0 ])



params=get_params()
url=None
name=None
mode=None


check_settings()
uname = vhd.getSetting('uname')
pwd   = vhd.getSetting('pwd')

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
        CHN(url)
elif mode==2:
        print "PAGE"
        INDEX(url,name)
elif mode==3:
        print "PAGE"
        VIDEO(url)
elif mode==4:
        print "SEARCH  :"+url
        SEARCH()
       
xbmcplugin.endOfDirectory(int(sys.argv[1]))