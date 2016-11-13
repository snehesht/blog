"use strict";
// ╳
var menubar = document.getElementById('boss-btn');
var contracted_menu = "☰";
var contracted_menu_mobile = "☰";
var expanded_menu_mobile = "☰";
var expanded_menu = "☰";
var full_menu = `
<div id="minions" class="anime">
	<ul>
		<li><a href="/">/root</a></li>
		<li><a href="/blog">/blog</a></li>
		<li><a href="/projects">/projects</a></li>
		<li><a href="/resume">/resume</a></li>
		<li><a href="/about">/about</a></li>
	</ul>
</div>
`;

function expand_menu(elem) {
	if (window.innerWidth < 768){
		var menu_elem = document.getElementById('postmenu');
		menu_elem.innerHTML = full_menu;
		elem.innerHTML = expanded_menu_mobile ;
	} else {
		var menu_elem = document.getElementById('premenu');
		menu_elem.innerHTML = full_menu;
		elem.innerHTML = expanded_menu ;
	}
};

function contract_menu(elem) {
	// hiddenmenubar.style = "display:none;"
	var menu_elem = document.getElementById('postmenu');
	menu_elem.innerHTML = "";
	var menu_elem = document.getElementById('premenu');
	menu_elem.innerHTML = "";
	if (window.innerWidth < 768){
		elem.innerHTML = contracted_menu_mobile;
	} else {
		elem.innerHTML = contracted_menu;
	}
};

function toggle_menu(elem) {
	elem.state.change = elem.state.change+1;
	elem.state.current_state = !elem.state.current_state;

	// Store object in HTML5 localstage
	// localStorage.setItem('menustate', JSON.stringify(elem.state));

	// console.log(elem.state);
	if (elem.state.change == 0 && elem.state.deault == false) {
		expand_menu(elem);
	} else if (elem.state.change !=0 &&  elem.state.current_state == true) {
		expand_menu(elem);
	} else if (elem.state.change !=0 &&  elem.state.current_state == false) {
		contract_menu(elem);
	}
}

menubar.onclick = function () {
	if(this.state == undefined ){
		// console.log('inital state');
		// var retrive_state = localStorage.getItem('menustate');
		// if (retrive_state == null) {
		// 	this.state = {
		// 					"current_state": false, // both current_state and default should be opposite
		// 					// true for expanded and false for contracted
		// 					"default": false, // always start as contracted menu
		// 					"change": true
		// 				};
		// 	} else {
		// 		this.state = JSON.parse(retrive_state);
		// 	};
		this.state = {
						"current_state": false, // both current_state and default should be opposite
						// true for expanded and false for contracted
						"default": false, // always start as contracted menu
						"change": 0
					};
	};
    toggle_menu(this);
};

// Index Page Dynamic Content Injection
function injector() {
	var dynblk_msg = "Hello, I'm Snehesh Thalapaneni, a full stack developer living in New York City.";
	setInterval(function(){
		var dynblk = document.getElementById('dyn-block');
		if (dynblk.innerHTML.length != dynblk_msg.length) {
			dynblk.innerHTML = dynblk.innerHTML + dynblk_msg[dynblk.innerHTML.length];
		};
	},200);
	setInterval(function(){
		var dyncursor = document.getElementById('dyn-cursor');
		dyncursor.style.display = dyncursor.style.display === 'none' ? '' : 'none';
	},150);
}
if (window.location.pathname == "/") {
	injector();
}
