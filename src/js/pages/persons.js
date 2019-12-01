$(document).ready(function() {
	function HideRemovedPersons()
	{
		$('#maintable tr > td.removedPerson').each(function () {
			$(this).parent().hide();
		});
	}
	function ShowRemovedPersons()
	{
		$('#maintable tr > td.removedPerson').each(function () {
			$(this).parent().show();
		});
	}

	$('#showRemovedPersons').click(function(event) {
		var button = $(event.target);
		if (button.hasClass('active'))
		{
			HideRemovedPersons();
		}
		else
		{
			ShowRemovedPersons();
		}
	});

	table = $('#maintable').DataTable( {
		"pageLength": 250,
        "language": {
			"sEmptyTable": "Tabellen innehåller ingen data",
			"sInfo": "Visar _START_ till _END_ av totalt _TOTAL_ rader",
			"sInfoEmpty": "Visar 0 till 0 av totalt 0 rader",
			"sInfoFiltered": "(filtrerade från totalt _MAX_ rader)",
			"sInfoPostFix": "",
			"sInfoThousands": " ",
			"sLengthMenu": "Visa _MENU_ rader",
			"sLoadingRecords": "Laddar...",
			"sProcessing": "Bearbetar...",
			"sSearch": "Sök:",
			"sZeroRecords": "Hittade inga matchande resultat",
			"oPaginate": {
				"sFirst": "Första",
				"sLast": "Sista",
				"sNext": "Nästa",
				"sPrevious": "Föregående"
			},
			"oAria": {
				"sSortAscending": ": aktivera för att sortera kolumnen i stigande ordning",
				"sSortDescending": ": aktivera för att sortera kolumnen i fallande ordning"
			}
		}
		} );

		HideRemovedPersons();
});
