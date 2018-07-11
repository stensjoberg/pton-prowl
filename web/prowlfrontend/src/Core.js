import React, { Component } from 'react'
import { Route, Redirect } from 'react-router-dom'
import Radium from 'radium'
import CourseItemList from './CourseItemList'
import Whenisgood from './Whenisgood'
import LogoutForm from './LogoutForm'
import CourseDetail from './CourseDetail'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';

class Core extends Component {

  render() {
    if (localStorage.getItem('token') == null) {
      return (<Redirect to="/login" />);
    }
    else {
      return (
        <div className="flexcontainer hor">
          <CourseItemList/>
          <Whenisgood/>
          <LogoutForm history={this.props.history}/>
          <Route path='/course/:courseId' component={CourseDetail}/>
        </div>
      )
    }
  }
}

export default Radium(Core)
