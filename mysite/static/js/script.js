// JavaScript Document

window.onload = function() {
	var rblist = document.getElementsByClassName("report-box");
	var rb_content = rblist.childNodes;
	
	for (var i = 0; i < rblist.length; i++) {
		rblist[i].onclick = function(e) {
			var el = e.target;
			switch (el.className) {
				case 'close':
					removeNode(el.parentNode);
				case 'comment-operate':
					operateComment(el);
				case 'btn':
					replyBox(el.parentNode.parentNode.parentNode);
				
			}
		}



		var textarea = document.getElementsByClassName("comment")[i];
		textarea.onfocus = function() {
			this.parentNode.className += " textbox-focus";
			this.className += " comment-focus";
			this.value = this.value == "Comments" ? "" : this.value;
		}
		textarea.onblur = function() {
			if (this.value == ""){
				this.parentNode.className = this.parentNode.className.replace( /(?:^|\s)textbox-focus(?!\S)/g , '' );
				this.className = this.className.replace( /(?:^|\s)comment-focus(?!\S)/g , '' );
			}
		}
	}



//delete comment
	function operateComment(el){
		var commentList = el.parentNode.parentNode;
		var commentBox = commentList.parentNode.parentNode.parentNode;
		var commentText = commentBox.getElementsByTagName('textarea')[0];
		var user = commentList.getElementsByClassName("user")[0];
		var txt = el.innerHTML;
		if (txt == 'reply') {
			commentText.onfocus();
			commentText.value = 'Reply to ' + user.innerHTML;
		} else {
			removeNode(commentList);
		}


	}
	
	
}



//remove a node
function removeNode(node) {
	node.parentNode.removeChild(node);
}


//
function replyBox(box) {
	var text = box.getElementsByClassName('comment')[0];
	var list = box.getElementsByTagName('ul')[0];
	var li = document.createElement('li');
	li.className = "comment-list-content";
	var html = '<p class="comment-text"><span class="user">userfoo:</span>'+ text.value +'</p>' +
				'<p class="comment-time">' +
				'2014-02-19 14:36' +
				'<a href="javascript:;" class="comment-like" total="0" my="0" style=""> </a>'+
				'<a href="javascript:;" class="comment-operate">delete</a>' +  '</p>';
	li.innerHTML = html;
	list.appendChild(li);
}



function replaceContentInContainer(matchClass, content) {
    var elems = document.getElementsByTagName('*'), i;
    for (i in elems) {
        if((' ' + elems[i].className + ' ').indexOf(' ' + matchClass + ' ')
                > -1) {
            elems[i].innerHTML = content;
        }
    }
}