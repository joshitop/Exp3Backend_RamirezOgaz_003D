$(document).ready(function()
{
    $("#solicitar").click(function(){

        $.get("https://mindicador.cl/api",
            function(data){

                $.each(data,function range(i, item){

                        var uf = item.nombre == 'Unidad de fomento (UF)';
                        var eur = item.nombre == 'Euro';
                        var bit = item.nombre == 'Bitcoin';
                        var dol = item.nombre == 'Dólar observado';


                        /*var vuf =  parceint(item.valor) ;
                        var veur = parceint(item.valor) ;
                        var vbit = parceint(item.valor) ;
                        var vdol = parceint(item.valor) ;*/


                        if (bit || uf || dol || eur) {

                            $("#monedas").append("<tr id='cualquiera'><td>"+item.nombre +"</td><td>"+ item.valor+ "</td></tr>");

                        }             

                });

        });
    });
})
