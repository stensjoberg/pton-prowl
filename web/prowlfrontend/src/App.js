// App.js
import React, { Component } from 'react'
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'
import Radium from 'radium'
import Core from './Core'
import LoginForm from './LoginForm'

import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';


class App extends Component {
  render() {
    return (
      <Router>
        <Switch>
          <Route path="/login" component={LoginForm} />
          <Route path="/" component={Core} />
        </Switch>
      </Router>
    );
  }
}

export default Radium(App)
