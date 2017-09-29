// Enables the scan button on the server subnet page
function servers_add_subnetscan_scan()
{
    $('body').on('click', '#servers_add_subnetscan_scan', function(event)
    {
        event.preventDefault();
        event.stopPropagation();
        ui_show_notification('Scanning!', 'is-danger');
    });
}

// Enables UI actions for notifications
function ui_enable_notifications()
{
    $('body').on('click', '.notification .delete', function(event)
    {
        event.preventDefault();
        event.stopPropagation();
        $(this).parent().fadeOut();
    });
}

// Displays a notification. Requires a #notifications container
// on the page
function ui_show_notification(text, type='is-primary')
{
    $('#notifications').append('<div class="notification ' + type + '"><button class="delete"></button>' + text + '</div>')
}



// Let's do this!
$(function()
{
    // Servers 
    servers_add_subnetscan_scan();

    // Generic UI elements
    ui_enable_notifications();

});
