<template>
    <div class="container mt-5">
      <h2 class="mb-4">Dados relevantes do CSV</h2>
      <table class="table table-bordered table-striped">
        <thead>
          <tr>
            <th scope="col">CNPJ</th>
            <th scope="col">Nome Fantasia</th>
            <th scope="col">Razão Social</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in tableData" :key="index">
            <td>{{ item.CNPJ }}</td>
            <td>{{ item.Nome_Fantasia }}</td>
            <td>{{ item.Razao_Social }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    name: "TabelaProfissional",
    data() {
      return {
        tableData: [],
      };
    },
    mounted() {
        this.fetchData();
  },
    methods: {
        fetchData() {
            fetch('http://localhost:5000/data')
            .then((response) => response.json())
            .then((data) => {
                this.tableData = data
            })
            .catch((error) => {
                console.error("Erro ao buscar os dados:", error);
            })
        }
    }
  };
  </script>
  
  <style scoped>
  .table thead {
    background-color: #343a40;
    color: white;
  }
  
  .table th,
  .table td {
    vertical-align: middle;
  }
  
  .table tbody tr:nth-child(odd) {
    background-color: #f8f9fa;
  }
  
  .table tbody tr:hover {
    background-color: #e2e6ea;
  }
  </style>
  