import React, { Component } from 'react'
import { Route, Redirect } from 'react-router-dom'
import Radium from 'radium'
import CourseItemList from './CourseItemList'
import Whenisgood from './Whenisgood'
import { isAuthenticated } from './LoginForm'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';

class Core extends Component {

  render() {
    if (!isAuthenticated()) {
      return (<Redirect to="/login" />);
    }
    return (
      <div className="flexcontainer hor">
        <CourseItemList/>
        <Whenisgood/>
        <Route path='/course/:courseId' component={Course}/>
      </div>
    )
  }
}

const Course = ({ match }) => {
  return <h1>Placeholder: {match.params.courseId}!</h1>
}

export default Radium(Core)
