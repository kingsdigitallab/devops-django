// JQuery Overrides

// We want :contains to be case insensitive
jQuery.expr[':'].contains = function(a, i, m) {
  return jQuery(a).text().toUpperCase()
      .indexOf(m[3].toUpperCase()) >= 0;
};

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

// Enables UI quick search
// Usage: class="quick-search" data-target="#id-to-search>child"
// If no results are found, it shows the element "#is-empty"
function ui_enable_quick_search()
{
    $('body').on('keyup', '.quick-search', function(event)
    {
        var target = $($(this).attr('data-target') + ':not(#quick-search-is-empty)');
        var empty = $($(this).attr('data-target') + '#quick-search-is-empty');
        if (event.keyCode === 27)
        {
            // Escape
            $(this).val('');
            $(target).show();
        } else
        {
            var val = $(this).val()

            $(target).show();
            $($(this).attr('data-target') + ':not(:contains(' + val + '))').hide();
        }

        if ($( $(this).attr('data-target') + ':visible').length == 0)
        {
            $(empty).show();
        } else
        {
            $(empty).hide();
        }
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
    ui_enable_quick_search();

});
