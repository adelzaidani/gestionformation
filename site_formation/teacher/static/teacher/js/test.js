$('#table_attendance tr').each(function(row,tr){
    table_data=table_data
    + $(tr).find('td:eq(0)').text();
    if ($(tr).find('td:eq(1)').('input:checkbox')attr('checked')){
          table_data = table_data + 'true';

    }

    else{
        table_data = table_data + 'true';
    }
    alert(table_data);
)};
