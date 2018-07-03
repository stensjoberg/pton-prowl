// App.js
import React, { Component } from 'react'
import { BrowserRouter as Router, Route } from 'react-router-dom'
import Radium from 'radium'
import CourseItemList from './CourseItemList'
import Whenisgood from './Whenisgood'
import LoginForm from './LoginForm'
import { styles } from './styles'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';

class App extends Component {
  render() {
    return (
      <Router on>
        <Route
          path="/"
            render={() => !isAuthenticated() ?
              <LoginForm/> :
              <div className="flexcontainer hor">
                <CourseItemList/>
                <Whenisgood/>
                <Route path='/course/:courseId' component={Course}/>
              </div>
            }/>
      </Router>
    );
  }
}

const Course = ({ match }) => {
  return <h1>Placeholder: {match.params.courseId}!</h1>
}

function isAuthenticated() {
  // TODO: implement this
  return true
}

export default Radium(App)
