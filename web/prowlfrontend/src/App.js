// App.js
import React, { Component } from 'react'
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'
import Radium from 'radium'
import Core from './Core'
import LoginForm from './LoginForm'
import UserDetail from './UserDetail'
import CourseDetail from './CourseDetail'

import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';


class App extends Component {
  render() {
    return (
      <Router>
        <Switch>
          <Route path="/login" component={LoginForm}/>
          <Route path="/courses" component={Core}/>
          <Route path='/user/:netid' component={UserDetail}/>
        </Switch>
      </Router>
    );
  }
}

export default Radium(App)
