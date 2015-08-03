function hasThoseClasses(classNames, event){
	if (classNames != null){
		$.each(classNames, function(i, className1){
			if (!$(event).hasClass(className1)){
				$(event).hide();
				return false;
			}				
		});
	}
	
		
}
function refreshEvents(fieldsArray, timeInDayArray, dayInWeekArray){
	var events = $(".events");
	events.show();

	$.each(events, function(i, event){	
		$.each(fieldsArray, function(i, field) { hasThoseClasses($(field).val(), event); });
		if (!$(event).is(":visible"))
			return false;
		$.each(timeInDayArray, function(i, time) { hasThoseClasses($(time).val(), event); });
		if (!$(event).is(":visible"))
			return false;
		$.each(dayInWeekArray, function(i, day) { hasThoseClasses($(day).val(), event); });
	});
	alert($(fieldsArray).val() + " " + $(timeInDayArray).val() + " " + $(dayInWeekArray).val());
}

