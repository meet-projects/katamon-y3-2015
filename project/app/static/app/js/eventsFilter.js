function hasAtLeastOneClass(classesNames, event){
	var passFilter = true;
	if (classesNames != null){
		passFilter = false;
		$.each(classesNames, function(i, className){
			if ($(event).hasClass(className)){
				passFilter = true;
				return false;
			}				
		});
					console.log("filter: " + JSON.stringify(classesNames)); 
	}
	return passFilter
}

function matchThisFilter(filterGroup, event){
	var returnValue = false;
	
	//console.log("filter group class: " + JSON.stringify(filterGroup));

	$.each(filterGroup, function(i, filter) { 
		console.log("filter group: " + JSON.stringify(filter)); 
		if (hasAtLeastOneClass($(filter).val(), event)){
			returnValue = true;
			return false;	
		}

	});
	return returnValue;
}

function refreshEvents(fieldsArray, timeInDayArray, dayInWeekArray){
	var events = $(".events");

	$.each(events, function(i, event){	
/*
		$.each(fieldsArray, function(i, field) { hasThoseClasses($(field).val(), event); });
		if (!$(event).is(":visible"))
			return;
		$.each(timeInDayArray, function(i, time) { hasThoseClasses($(time).val(), event); });
		if (!$(event).is(":visible"))
			return;
		$.each(dayInWeekArray, function(i, day) { hasThoseClasses($(day).val(), event); });
*/
		var fieldCheck = matchThisFilter(fieldsArray, event);
		var timeCheck = matchThisFilter(timeInDayArray, event);
		var dayCheck = matchThisFilter(dayInWeekArray, event);

		if (fieldCheck && timeCheck && dayCheck){
			$(event).slideDown();
		}
		else{
			$(event).slideUp();
		}

	});
}

