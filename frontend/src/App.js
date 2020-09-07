import React, { Component } from 'react'
import Header from './components/Header'
import { BrowserRouter as Router, Switch, Route} from "react-router-dom";
import Home from "./components//Home";
import About from "./components//About";
import Gallery from './components//Gallery'
import Login from "./components/Login";


class App extends Component {
  render() {
    return (
      <div>
        <Router>
        <Header />

        <Switch>
            <Route exact path="/" component={Home} />
            <Route path="/about" component={About} />
            <Route path="/gallery" component={Gallery} />
            <Route path="/userlogin" component={Login} />
            
          </Switch>
        </Router>
      
      </div>
    )
  }
}

export default App
