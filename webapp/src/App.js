import './App.css';

import Header from './components/header/header';
import Info from './components/info/info';
import Input from './components/input/input';
import Keyboard from './components/keyboard/keyboard';

import SearchPage from './pages/search-page';

function App() {
  return (
    <div className="App">
      <SearchPage/>
    </div>
  );
}

export default App;
