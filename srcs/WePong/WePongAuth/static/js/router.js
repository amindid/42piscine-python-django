const route = (event) => {
	event = event || window.event;
	event.preventDefault();
	window.history.pushState({}, "", event.target.href);
	handleLocation();
}

const routes = {
	"/" : "/",
	"login" : "login",
	"registration" : "registration",
}

const handleLocation = async () => {
	const path = window.location.pathname;
	console.log("path ===> ",path)
	const route = routes[path] || routes["login"];
	console.log("route ===> ",route)
	const html = await fetch(route).then((data) => data.text());
	document.getElementById("root").innerHTML = html;
}

window.onpopstate = handleLocation;
window.route = route;

handleLocation();

/*
window.pathname => handleLocation(--)
event listener a tag (href value) => handle location
 */