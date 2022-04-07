from http.client import responses
from importlib.resources import contents
from pyhtml import ul,li
from Mainpage import Login_nvabar
def DisplayProfile(user, viwer, is_editting, passed_in):
    with open("./EditProfile.html", "r") as fl:
        contents = fl.readlines()
    is_ownner = False
    if user['email'] == viwer['email']:
        is_ownner = True
    else:
        is_editting = False
    contents.insert(63, display_good_at(user, is_editting))
    contents.insert(62, display_pereference(user, is_editting))
    contents.insert(61, display_WAM_pefered(user, is_editting))
    contents.insert(60, display_WAM(user, is_editting))
    if is_ownner and is_editting:
        contents.insert(59, display_password(user,passed_in))
    contents.insert(58, display_email(user))
    contents.insert(57, display_username(user, is_editting))
    contents.insert(52, display_self_introduction(user, is_editting))
    contents.insert(45, display_icon(user, is_editting))
    contents.insert(28, Login_nvabar(viwer['email']))

    response = ''.join(contents)
    return response


def display_username(user,is_editing):
    response = f"""
    <form action="mysetting" class="field" method="POST">
        <h4 class="field_item">User name: </h4>
        <p class="field_item">{user['username']}</p>
        
    """
    if is_editing:
        response += """
        <input type="text" " name="username" placeholder="New Username">
        <input type="submit" " value="Change" name="new_username">
    </form>
        """
    else:
        response += """
    </form>
        """
    return response

def display_email(user):
    return f"""
    <form action="mysetting" class="field" method="POST">
        <h4 class="field_item">E-mail: </h4>
        <a class="field_item" href="mailto:{user['email']}">{user['email']}</a>
        </form>
    """

def display_password(user, passwoed_entered):
    message = ""
    if 'old_password' in passwoed_entered and user['password'] != passwoed_entered['old_password']:
        message = "You are failed to change password as you typed wrong old password."
    return f"""
    <form action="mysetting" class="field" method="POST">
        <h4 class="field_item">Password Change: </h4><br>
        <h5 class="field_item">Old password:</h5>
        <input type="password" " name="o_password" placeholder="Your current password"><br>
        <h5 class="field_item">New password:</h5>
        <input type="password" " name="password" placeholder="Your new password">
        <input type="submit" " value="Change" name="new_password">
        <label style="color: tomato;"> {message} </label>

    </form>
    """
def display_WAM(user,is_editing):
    response = f"""
    <form action="mysetting" class="field" method="POST">
        <h4 class="field_item">WAM: </h4>
        <p class="field_item">{user['WAM']}</p>
        
    """
    if is_editing:
        response += """
        <input type="number" " name="WAM" placeholder="Your WAM" step="0.01" min="0" max="100">
        <input type="submit" " value="Change" name="new_WAM">
    </form>
        """
    else:
        response += """
    </form>
        """
    return response

def display_WAM_pefered(user,is_editing):
    response = f"""
    <form action="mysetting" class="field" method="POST">
        <h4 class="field_item">WAM perfered: </h4>
        <p class="field_item">{user['WAM_perfered']}</p>
        
    """
    if is_editing:
        response += """
        <input type="number" " name="WAM_pefered" placeholder="WAM of expected teammates" step="0.01" min="0" max="100">
        <input type="submit" " value="Change" name="new_WAM_pefered">
    </form>
        """
    else:
        response += """
    </form>
        """
    return response

def display_pereference(user, is_editing):
    p_list = [li(p) for p in user['perference']]
    response = f"""
    <form action="mysetting" class="field" method="POST">
        <h4 class="field_item">Pereference: </h4>
        {str(ul(p_list))}
    """
    if is_editing:
        response += f"""
        <input type="text" "name="perference" placeholder="Preference for teammates">
        <input type="submit" " value="Add" name="add_perference">
        <input type="submit" " value="Remove" name="remove_perference">
    </form>
        """
    else:
        response += """
    </form>
        """
    return response

def display_good_at(user, is_editing):
    p_list = [li(p) for p in user['good_at']]
    response = f"""
    <form action="mysetting" class="field" method="POST">
        <h4 class="field_item">Good at: </h4>
        {str(ul(p_list))}
    """
    if is_editing:
        response += f"""
        <input type="text" "name="good_at" placeholder="what you are good at">
        <input type="submit" " value="Add" name="add_good_at">
        <input type="submit" " value="Remove" name="remove_good_at">
    </form>
        """
    else:
        response += """
    </form>
        """
    return response
def display_icon(user, is_editing):
    editting = ""
    if is_editing:
        editting = """
        <label style="display: block;"> Change icon</label>
        <form action="mysetting" method="POST">
            <textarea name="iconlink" id="" cols="30" rows="5"></textarea>
            <input type="submit" name="new icon" value="Change", style="display: block;">
        </form>
        """
    return  f"""
    <img src="{user['icon_link']}" class="icon">
        {editting}
    """

def display_self_introduction(user, is_editing):
    editting = ""
    if is_editing:
        editting = f"""
        <form action="mysetting" method="POST">
            <textarea name="introduction" id="" cols="30" rows="5">Hi Guys, This is {user['username']}.</textarea>
            <input type="submit" name="new_introduction" value="Change", style="display: block; align:center">
        </form>
        """
    return  f"""
    <h4 style="box-sizing: border-box; width: 200px; border-bottom: 1px solid #ebebeb;">Brief Self introduction</h4>
    <p style=" width: 200px;border-right: 1px solid #cfd8dc; word-break:break-all;"> {user['introduction']} </p>

        {editting}
    """