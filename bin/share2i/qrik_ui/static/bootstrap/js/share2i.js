// background.js
chrome.contextMenus.create({
    title: "Share2i",
    onclick: function(info, tab){
    	chrome.tabs.create({'url': chrome.extension.getURL('popup.html')}, function(tab) {
    		 
		});
    }
});


