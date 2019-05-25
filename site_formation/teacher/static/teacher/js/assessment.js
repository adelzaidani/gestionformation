$('#save_assessment').click(function(){

    var tableAssessment;
    tableAssessment = saveTable()
    tableAssessment = $.toJSON(tableAssessment);

         $.ajaxSetup({async: false});
         $.ajax({
            type: "POST",
            url: "/teacher/save_assessment/",
            data: "tableAssessment=" + tableAssessment,
            success: function(data){
               if (data.exist) {
                    alert(data.message);
                }
                else{

                    alert(data.message);
                }

             }


         });

});

function saveTable(){
     var
        session=$('#num_session').val();
        tableAssessment = new Array();



       $('#table_assessment tr').each(function(row, tr){

             tableAssessment[row]={
                "id_client": $(tr).find('td:eq(0)').text(),
                 "session":session,
                 "assessment":$(tr).find('td:eq(4) input').val(),

             }

        });


tableAssessment.shift();
return tableAssessment;
};

