import React from 'react';
import DenseAppBar from './DenseAppBar.js';
import FooterBar from './FooterBar.js';
import Content from './Content.js';
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <DenseAppBar></DenseAppBar>
      </header>
      <section>
        <Content></Content>
      </section>
      <footer>
        <FooterBar></FooterBar>
      </footer>
    </div>
  );
}

export default App;
