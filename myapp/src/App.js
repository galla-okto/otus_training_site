import './App.css';
import React from "react";
import { Header } from "./components/Header";
import { Button} from "./components/Button";


class App extends React.Component {
  buttonClickHadler = () => {
    // alert("Hola")

    this.setState({
      valueX: 10
    });
    // this.state.valueX = 10;
  };

  state = {
    valueX: 4,
    someY: 123
  };

  render() {
    return (
      <div className="App">
        <Header value={this.state.valueX + 2} />
        <Button value={this.state.valueX} onButtonClick={this.buttonClickHadler()} />

        <pre>{JSON.stringify(this.state, null, 2)}</pre>
      </div>
    );
  }
}

export default App;
