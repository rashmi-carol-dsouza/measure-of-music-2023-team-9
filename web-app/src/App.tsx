import React from "react";
import "./App.css";
import Search from './Search';

function App() {
  return (
    <div className="App">
      <header className="header">
        <div className="header__container">
        <p className="logo">
          <span>Collaborata</span>
        </p>

        <h1>
          Find the <span className="text-aqua">perfect</span> match for your
          next <span className="text-green">collaboration</span> across the{" "}
          <span className="text-yellow">world.</span>
        </h1>
        </div>
      </header>

      <main>
        <p className="text-lead">Collaborata helps artists expand their global audience by matching them with international artists that would be a creative fit for collaborations.</p>
        <Search />
      </main>

      <footer>
        <small>Hacked with ❤️ by <a href="https://rashmidsouza.com/?src=mom2023">Rashmi DSouza</a>, <a href="https://de.linkedin.com/in/aaron-dutschmann">Aaron Dutschmann</a>, <a href="https://uk.linkedin.com/in/saskiaallan">Saskia Allan</a>, <a href="https://instagram.com/trustroy">Trust Meebelbari</a> and <a href="https://larrydalmeida.com/?lang=en&src=mom2023/">Larry D Almeida</a> at <a href="https://measureofmusic.com/">Measure of Music</a>, 2023</small>
      </footer>
    </div>
  );
}

export default App;
