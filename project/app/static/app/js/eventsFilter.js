function hasThoseClasses(className, event){
	if (!$(event).hasClass(className))
		$(event).hide();
	else
		$(event).show();
}
function refreshEvents(fieldsArray, timeInDayArray, dayInWeekArray){
	var events = $(".events");
	events.show();

	$.each(events, function(i, event){
		$.each(fieldsArray, function(i, field) { hasThoseClasses(field, event); });
		$.each(timeInDayArray, function(i, time) { hasThoseClasses(time, event); });
		$.each(dayInWeekArray, function(i, day) { hasThoseClasses(day, event); });
	});
}
$(function(){
	

});

