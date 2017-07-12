conn = new Mongo();
db = conn.getDB("mydb");

db.properties.find().snapshot().forEach( function(el) {
	el.Type = el.Type.split(",").map( function(item) { 
		return item.trim();
	});  
	db.properties.save(el);
});
