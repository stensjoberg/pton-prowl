// App.js
import React, { Component } from 'react'
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'
import Radium from 'radium'
import Core from './Core'
import LoginForm from './LoginForm'
import UserDetail from './UserDetail'
import Welcome from './Welcome'
import CourseDetail from './CourseDetail'
import Home from './Home'


import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';


class App extends Component {
  render() {
    return (
      <Router>
        <Switch>
          <Route path="/welcome" component={Welcome}/>
          <Route path="/login" component={LoginForm}/>
          <Route path="/home" component={Home}/>
          <Route path='/course/:courseId' component={CourseDetail}/>
          <Route path='/user/:netid' component={UserDetail}/>
        </Switch>
      </Router>
    );
  }
}

export default Radium(App)
