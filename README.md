<h1>📋 Lista de Tarefas</h1>

<p>
  Este projeto consiste em uma <strong>lista de tarefas hierárquica</strong>.
  Ele foi desenvolvido com o objetivo de praticar <strong>estruturas de dados</strong>,
  especialmente árvores.
</p>

<hr>

<h2>📌 Descrição do Projeto</h2>

<p>
  Este projeto implementa uma <strong>ToDo List hierárquica</strong>, baseada na
  estrutura de dados <strong>Árvore (Tree)</strong>.
</p>

<p>
  Ele permite organizar tarefas e subtarefas de forma estruturada,
  acompanhar o status de cada item e calcular automaticamente
  o <strong>progresso geral do projeto</strong>.
</p>

<p>
  A aplicação é executada via <strong>linha de comando (CLI)</strong> e foi
  desenvolvida em <strong>Python</strong>, com foco em lógica de estruturas de dados
  e recursão.
</p>

<hr>

<h2>🏗️ Estrutura do Projeto</h2>

<pre>
📁 projeto
 ├── ToDo.py              # Estrutura de dados e regras de negócio
 └── interface_do_user.py # Interface de interação com o usuário (CLI)
</pre>

<hr>

<h2>🧩 Componentes do Sistema</h2>

<h3>Enum Status</h3>
<p>
  Define os estados possíveis de uma tarefa:
</p>

<ul>
  <li><strong>not_concluded</strong> – tarefa ainda não iniciada</li>
  <li><strong>in_progress</strong> – tarefa em andamento</li>
  <li><strong>concluded</strong> – tarefa finalizada</li>
</ul>

<h3>Classe Node</h3>

<p>
  Representa uma <strong>tarefa ou subtarefa</strong>.
</p>

<p><strong>Atributos:</strong></p>
<ul>
  <li><strong>data</strong>: nome da tarefa</li>
  <li><strong>status</strong>: estado atual da tarefa</li>
  <li><strong>children</strong>: lista de subtarefas</li>
</ul>

<h3>Classe Tree</h3>

<p>
  Representa o <strong>projeto completo</strong>, onde:
</p>

<ul>
  <li>o nó raiz é o nome do projeto</li>
  <li>cada nó pode conter várias subtarefas</li>
</ul>

<p><strong>Principais métodos:</strong></p>

<ul>
  <li>
    <strong>add_child(parent, child_data)</strong><br>
    Adiciona uma subtarefa a uma tarefa existente.
  </li>
  <li>
    <strong>remove_child(parent, child_data)</strong><br>
    Remove uma tarefa e suas subtarefas.
  </li>
  <li>
    <strong>search(data)</strong><br>
    Busca recursivamente uma tarefa pelo nome.
  </li>
  <li>
    <strong>levelOrder()</strong><br>
    Retorna a lista de tarefas organizada por níveis (BFS).
  </li>
  <li>
    <strong>return_percentage()</strong><br>
    Calcula o percentual de progresso do projeto.
  </li>
</ul>

<hr>

<h2>🖥️ Interface com o Usuário (CLI)</h2>

<h3>🔰 Inicialização</h3>

<p>
  Ao iniciar o programa, o usuário define o nome do projeto:
</p>

<pre>Add the name of the project:</pre>

<h3>🔄 Menu de Opções</h3>

<pre>
1 - Add tasks
2 - Change task status
3 - End loop
</pre>

<hr>

<h2>✏️ Funcionalidades</h2>

<h3>✅ Adicionar tarefas e subtarefas</h3>

<ul>
  <li>Escolha de uma tarefa pai existente</li>
  <li>Inserção de múltiplas subtarefas separadas por vírgula</li>
  <li>Validação caso a tarefa não exista</li>
</ul>

<h3>🔄 Alterar status de tarefas</h3>

<ul>
  <li>Busca de tarefas pelo nome</li>
  <li>Alteração para:
    <ul>
      <li>in progress</li>
      <li>concluded</li>
    </ul>
  </li>
  <li>Tratamento de erro para tarefas inexistentes</li>
</ul>

<h3>⛔ Encerrar o programa</h3>

<ul>
  <li>Exibe a lista completa de tarefas</li>
  <li>Mostra o progresso total do projeto</li>
</ul>

<hr>

<h2>📋 Exemplo de Saída</h2>

<pre>
To do list:
['Projeto -> in_progres']
['Tarefa A -> concluded', 'Tarefa B -> in_progres']
['Subtarefa A1 -> concluded', 'Subtarefa A2 -> in_progres']

The progress of the project is in 66.6%
</pre>

<hr>

<h2>📈 Cálculo de Progresso</h2>

<p>
  O progresso do projeto é calculado automaticamente com base na
  proporção de tarefas concluídas:
</p>

<pre>
(concluded_tasks / total_tasks) * 100
</pre>

<p>
  <em>Obs.: o nó raiz (nome do projeto) não é considerado no cálculo final.</em>
</p>

<hr>

<h2>▶️ Como Executar</h2>

<pre>python interface_do_user.py</pre>

<hr>

<h2>🔮 Melhorias Futuras</h2>

<ul>
  <li>Persistência de dados (JSON ou Banco de Dados)</li>
  <li>Remoção de tarefas via menu</li>
  <li>Interface gráfica ou Web</li>
</ul>
