import React, { Component } from 'react'
import { Route, Redirect } from 'react-router-dom'
import Radium from 'radium'
import Helmet from 'react-helmet';
import NavBar from './NavBar'
import CourseItemList from './CourseItemList'
import LogoutForm from './LogoutForm'
import CourseDetail from './CourseDetail'
import UserDetail from './UserDetail'
import Availability from './Availability'
import { getUser } from './helper.js'
import './css/stylesheet.css';
import './css/normalize.css';
import './css/skeleton.css';


class Home extends Component {

    state = {
        user: {}
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
    if (this.state.user.availability === undefined) {
        return false
    }
      else {
          return (
              <div>
                <Helmet bodyAttributes={{style: 'background-color : #EAEAEA'}}/>
                <NavBar user={this.state.user} history={this.props.history}/>
                <div className="flexcontainer hor top">
                    <CourseItemList className="courseitemlist"/>
                    <Availability data={this.state.user.availability}/>
              </div>
              </div>
          )
      }
  }
}

export default Radium(Home)
