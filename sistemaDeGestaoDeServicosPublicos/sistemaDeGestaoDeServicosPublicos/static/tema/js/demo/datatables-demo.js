// Call the dataTables jQuery plugin
$(document).ready(function () {
  $('table').DataTable({
    "order": [],
    "lengthChange": true,
    "lengthMenu": [[5, 10, 20, 30, 40, 50, 100, -1], [5, 10, 20, 30, 40, 50, 100, "Todos"]],
    colReorder: true,
    responsive: true,
    dom: 'lBfrtip',
    buttons: [
      'print',
      'excel',
      'pdf',
      // 'colvis'
    ],
    "language": {
      "sEmptyTable": "Nenhum registro encontrado",
      "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
      "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
      "sInfoFiltered": "(Filtrados de _MAX_ registros)",
      "sInfoPostFix": "",
      "sInfoThousands": ".",
      "sLengthMenu": "_MENU_ resultados por página",
      "sLoadingRecords": "Carregando...",
      "sProcessing": "Processando...",
      "sZeroRecords": "Nenhum registro encontrado",
      "sSearch": "Pesquisar",
      "oPaginate": {
        "sNext": "Próximo",
        "sPrevious": "Anterior",
        "sFirst": "Primeiro",
        "sLast": "Último"
      },
      "oAria": {
        "sSortAscending": ": Ordenar colunas de forma ascendente",
        "sSortDescending": ": Ordenar colunas de forma descendente"
      },
      "select": {
        "rows": {
          "_": "Selecionado %d linhas",
          "0": "Nenhuma linha selecionada",
          "1": "Selecionado 1 linha"
        }
      },
      "buttons": {
        "copy": "Copiar",
        "copyTitle": "Cópia bem sucedida",
        "copySuccess": {
          "1": "Uma linha copiada com sucesso",
          "_": "%d linhas copiadas com sucesso"
        },
        'print': 'Imprimir',
        'pdf': 'Salvar .PDF',
        'excel': 'Salvar .xlxs',
        'colvis': 'Colunas'
      }
    }


  });
});
