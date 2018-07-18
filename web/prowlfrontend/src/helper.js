export async function getCourse({ id, url }) {

    if (id !== undefined && url === undefined) {
        url = 'http://0.0.0.0:8000/api/v1/courses/' + id
    }
    try {
        const response = await fetch(url, {
            headers: {
                'Authorization': 'Token ' + localStorage.getItem('token'),
            }
        }
        )
        const course = await response.json()
        return course
    } catch (e) {
        console.log(e)
    }
}

export async function getAllCourses() {

    const url = 'http://0.0.0.0:8000/api/v1/courses/'
    try {
        const response = await fetch(url, {
            headers: {
                'Authorization': 'Token ' + localStorage.getItem('token'),
            }
        }
        )
        const courses = await response.json()
        return courses
    } catch (e) {
        console.log(e)
    }
}



export async function getUser(netid) {

    if (netid === undefined) {
        try {
            const response = await fetch('http://0.0.0.0:8000/api/v1/validate', {
                headers: {
                    'Authorization': 'Token ' + localStorage.getItem('token'),
                }
            })
            const user = await response.json()
            return user
        } catch (e) {
            console.log(e)
        }
    }
    else {
        try {
            const response = await fetch('http://0.0.0.0:8000/api/v1/users/' + netid, {
                headers: {
                    'Authorization': 'Token ' + localStorage.getItem('token'),
                }
            })
            const user = await response.json()
            return user
        } catch (e) {
            console.log(e)
        }
    }

}

export async function getCoursesFromLinks(links) {
    let objects = []
    for (let i in links) {
        objects.push(await getCourse({ url: links[i] }))
    }
    return objects
}
