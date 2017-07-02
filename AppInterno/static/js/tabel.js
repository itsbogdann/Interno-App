$(document).ready(function()
{

    var el = $('#tabel_contracte');

     el.find('tfoot th').each( function () {
        var title = $(this).text();
        $(this).html( '<input type="text" placeholder="Cauta '+title+'" />' );
    } );

     $.fn.dataTable.moment( 'D MMMM YYYY','ro');

     var tabel = el.DataTable(
     {
         "language": {
                     "url": "//cdn.datatables.net/plug-ins/1.10.13/i18n/Romanian.json"
                     },
        "scrollY": "72vh",
        "order": [[ 2, "desc" ]],
        columnDefs: [{ orderable: false, targets: [5] }],
        "scrollCollapse": true,
        initComplete: function(){
              tabel.columns().every( function () {
              var that = this;
              $( 'input', this.footer() ).on( 'keyup change', function () {
              if ( that.search() !== this.value ) {
                    that
                    .search( this.value )
                    .draw();
                 }
                });
               });
             }
     });

 });