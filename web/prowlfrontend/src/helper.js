export async function getCourse({ id, url }) {

    if (id !== undefined && url === undefined) {
        url = 'http://0.0.0.0:8000/api/v1/courses/' + id
    }
    console.log(url)
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

export async function getUser(netid) {
    console.log(netid)

    if (netid === undefined) {
        try {
            const response = await fetch('http://0.0.0.0:8000/api/v1/validate', {
                headers: {
                    'Authorization': 'Token ' + localStorage.getItem('token'),
                }
            })
            console.log(response)
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

export async function getObjectsFromLinks(links) {
    let objects = []
    for (let i in links) {
        objects.push(await getCourse({ url: links[i] }))
    }
    return objects
}
