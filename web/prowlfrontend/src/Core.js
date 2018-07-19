import React, { Component } from 'react'
import { Route, Redirect } from 'react-router-dom'
import Radium from 'radium'
import NavBar from './NavBar'
import CourseItemList from './CourseItemList'
import LogoutForm from './LogoutForm'
import CourseDetail from './CourseDetail'
import UserDetail from './UserDetail'
import { getUser } from './helper.js'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';

class Core extends Component {

    state = {
        user: Object()
    }

    async componentDidMount() {

        const user = await getUser()
        this.setState({
            user
        })
    }

  render() {
    if (localStorage.getItem('token') == null) {
      return (<Redirect to="/login" />);
    }

      else {
          return (
              <div>
                <NavBar user={this.state.user} history={this.props.history}/>
                <div className="flexcontainer hor" className="left">
                <CourseItemList className="courseitemlist"/>
                <Route className="coursedetail" path='/courses/:courseId' component={CourseDetail}/>
              </div>
              </div>
          )
      }

  }
}

export default Radium(Core)
