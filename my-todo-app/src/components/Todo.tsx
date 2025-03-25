import { useState } from 'react';
import { Button, Form, ListGroup, Card } from 'react-bootstrap';

interface TodoItem {
  id: number;
  text: string;
  completed: boolean;
}

export default function Todo() {
  const [todos, setTodos] = useState<TodoItem[]>([]);
  const [input, setInput] = useState('');

  const addTodo = () => {
    if (input.trim()) {
      setTodos([...todos, { id: Date.now(), text: input, completed: false }]);
      setInput('');
    }
  };

  const toggleTodo = (id: number) => {
    setTodos(todos.map(todo => 
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
  };

  return (
    <Card className="m-3 p-3">
      <h1 className="text-center mb-4">Todo List</h1>
      
      <div className="d-flex mb-3">
        <Form.Control
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Новая задача"
        />
        <Button variant="primary" onClick={addTodo} className="ms-2">
          Добавить
        </Button>
      </div>

      <ListGroup>
        {todos.map(todo => (
          <ListGroup.Item 
            key={todo.id} 
            action 
            onClick={() => toggleTodo(todo.id)}
            className={todo.completed ? 'text-decoration-line-through' : ''}
          >
            {todo.text}
          </ListGroup.Item>
        ))}
      </ListGroup>
    </Card>
  );
}
